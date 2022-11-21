from bs4 import BeautifulSoup
from urllib.request import urlopen
import feedparser
from email.generator import Generator
import imapclient
import email
from email.header import decode_header
import re
import pandas as pd
from datetime import timedelta
from tools.telegram_bot.contents import Context
       
class SrcFunction:  
      class Nber:      
        @staticmethod
        def squeezeDate(text:str):
                """
                text='Foreign Exchange Rates. Release time is 4 p.m. EDT.'
                squeezeDate(text)
                >> '4:00 p.m. EDT.'
                
                text='CFNAI. Release time is 8:30 a.m. EDT.'
                squeezeDate(text)
                >> '8:30 a.m. EDT.'
                """
                releaseDate=[]
                date = text.split('Release time is ')[-1]
                for i, d in enumerate(date.split()):
                    if i ==0:
                        if len(d.split(':')) <2: d = d+ ':00'
                    releaseDate.append(d)       
                return ' '.join(releaseDate)
  
      class MailBox:
            @staticmethod
            def get_UIDs_msg(usr:str, pid:str, box:str, imap:str ='imap.naver.com'):
                imap_obj = imapclient.IMAPClient(imap, ssl=True)
                imap_obj.login(usr, pid)
                imap_obj.select_folder(box, readonly=True)
                UIDs = imap_obj.search(['ALL'])
                raw_msg = imap_obj.fetch(UIDs, ['BODY[]'])
                return UIDs, raw_msg
              
            @staticmethod
            def get_news_from_box(usr:str, pid:str, box:str, sender:str, botChatId=None)-> Context:
                UIDs, raw_msg = SrcFunction.MailBox.get_UIDs_msg(usr, pid, box)
                for UID in UIDs[-20:]:  # 최근 20개만 읽음
                    message = email.message_from_bytes(raw_msg[UID][b'BODY[]'])
                    fr = decode_header(message.get('From'))
                    if  sender in str(fr):
                        if message.is_multipart():
                            for part in message.walk():
                                ctype = part.get_content_type()
                                cdispo = str(part.get('Content-Disposition'))
                                if ctype == 'text/plain' and 'attachment' not in cdispo:
                                    body = part.get_payload(decode=True)  # decode
                                    break
                        else:
                            body = message.get_payload(decode=True)
                        body = body.decode('utf-8')
                        url = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', body)[-11]
                        yield Context(content=[url], botChatId=botChatId)


class SrcGenerator:
  class HTML:
    def __init__(self):
      pass
    
    @staticmethod    
    def get_from_web(url, attr_key, prefix=None, botChatId=None)-> Context:
      headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
      for headline in headlines:  ## html의 속성 부분을 추출
        for link in headline.find_all('a'):
          if 'href' in link.attrs and (link.attrs['href'].startswith('http') or link.attrs['href'].startswith('www')):
            if prefix is not None: yield Context(content=[prefix + link.attrs['href']], botChatId=botChatId)
            else: yield Context(content=[link.attrs['href']], botChatId=botChatId)

    @staticmethod
    def get_from_web_without_http(url, attr_key, prefix=None, botChatId=None)-> Context:
      headlines = BeautifulSoup(urlopen(url), 'html.parser').find_all(attrs={'class':f'{attr_key}'})  # name은 태그 추출
      for headline in headlines:  ## html의 속성 부분을 추출
        for link in headline.find_all('a'):
          if 'href' in link.attrs:  #속성 중 링크만 추출
            if prefix is not None: yield Context(content=[prefix + link.attrs['href']], botChatId=botChatId)
            else: yield Context(content=[link.attrs['href']], botChatId=botChatId)
 
    @staticmethod
    def get_from_web_with_selector(url, selector, botChatId=None)-> Context:
      headlines = BeautifulSoup(urlopen(url), 'html.parser').select(selector) 
      for headline in headlines:  ## html의 속성 부분을 추출
        if 'href' in headline.attrs:  #속성 중 링크만 추출
          yield Context(content=[headline.attrs['href']], botChatId=botChatId)

    @staticmethod
    def get_from_web_link(url, class_key, botChatId=None)-> Context:
      links = BeautifulSoup(urlopen(url), 'html.parser').find_all('a')
      for link  in links:
        if 'class' in link.attrs:  #속성 중 class만 추출
          if class_key in link.attrs['class']:
            yield Context(content=[link.attrs['href']], botChatId=botChatId)
            
            
  class MailBox:
      def __init__(self):
          pass
      
      @staticmethod
      def wsj_news_from_mailbox(usr:str, pid:str, botChatId=None)-> Context:
          return SrcFunction.MailBox.get_news_from_box(usr, pid, box ='WSJ', sender="WSJ Follow Alert", botChatId=botChatId)
      
      @staticmethod
      def whale_wisdom_from_mailbox(usr:str, pid:str, botChatId=None)-> Context:
          return SrcFunction.MailBox.get_news_from_box(usr, pid, box ='whale_wisdom', sender="Whalewisdom.com", botChatId=botChatId)
     
        
  class Rss:
    # ============================================
    # 구글 알리미
    # ============================================
    @staticmethod
    def get_from_rss_feed_by_google(rss_url, botChatId=None)-> Context:
      try: 
        for feed in feedparser.parse(rss_url).entries:
          yield Context(content=[feed.link.replace('https://www.google.com/url?rct=j&sa=t&url=','').split('&ct=ga&cd')[0]], botChatId=botChatId)
      except: return

    # ============================================
    # RSS 피드
    # ============================================
    @staticmethod
    def get_from_rss_feed(rss_url, botChatId=None)-> Context:
      for feed in feedparser.parse(rss_url).entries:
        yield Context(title=feed.title, content=[feed.link], descr=feed.description, botChatId=botChatId)
        
    # ============================================
    # NBER RSS 피드
    # ============================================ 
    @staticmethod
    def get_from_rss_NBER_schedule(rss_url, botChatId=None)-> Context:
      for feed in feedparser.parse(rss_url).entries:
        # release_time = pd.to_datetime(SrcFunction.Nber.squeezeDate(feed.description)).date()+ timedelta(hours=13)
        # release_time =None
        yield Context(title=feed.title, content=[feed.link], descr=feed.description, key=feed.title, botChatId=botChatId)
 