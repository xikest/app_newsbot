from typing import Optional, Generator
from tools.telegram_bot.contents import Context
import imapclient
import email
from email.header import decode_header
import re
from tools.telegram_bot.contents import Context
from bs4 import BeautifulSoup
from selenium import webdriver
import asyncio

class SrcMailBox:
    
    
    SLEEP = False
    AWAKE = True
    status = SLEEP
    
    def __init__(self, usr:str, pid:str, mailings:Generator, ChatId:str=None):
        self._usr = usr
        self._pid = pid
        self._mailings = mailings
        self._ChatId:Optional[str]=ChatId

    async def generator(self)-> Context:
        if SrcMailBox.status == SrcMailBox.AWAKE:
                try:
                    for mailing in self._mailings():        
                        UIDs, raw_msg = self._get_UIDs_msg( self._usr, self._pid, mailing.box)
                        for UID in UIDs[-20:]:  # 최근 20개만 읽음
                            message = email.message_from_bytes(raw_msg[UID][b'BODY[]'])
                            fr = decode_header(message.get('From'))
                            if  mailing.sender in str(fr):
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
                                
                                if mailing.box == 'WSJ': 
                                    summary = Wsj(url).summary()
                                    enable_translate=True
                                else:
                                    summary = None
                                    enable_translate=False
                                
                                # print(enable_translate)
                                # print(summary)
                                    
                                yield Context(content=[url], label=f'{mailing.box}', summary=[summary], enable_translate=enable_translate, botChatId=self._ChatId, dtype='msg')
                except Exception as e:
                    print(f"mail box error: {e}")
                    SrcMailBox.status = SrcMailBox.SLEEP
                    await asyncio.sleep(30*60)
                    SrcMailBox.status = SrcMailBox.AWAKE
                    pass
                    
    def _get_UIDs_msg(self, usr:str, pid:str, box:str, imap:str ='imap.naver.com'):
        imap_obj = imapclient.IMAPClient(imap, ssl=True)
        imap_obj.login(usr, pid)
        imap_obj.select_folder(box, readonly=True)
        UIDs = imap_obj.search(['ALL'])
        raw_msg = imap_obj.fetch(UIDs, ['BODY[]'])
        return UIDs, raw_msg
    
    
    
    


class Wsj:
    """
    from tools.translate.papago import Papago
    papago = Papago('en')
    result = papago.translate('hello, today is a good day')
    papago.quit()
    print(result)

    """
    def __init__(self, url:str):
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--remote-debugging-port=9230")
        chrome_options.add_argument('user-agent={0}'.format(user_agent))
        chrome_options.add_argument('lang=ko_kr')
        
        self._wd = webdriver.Chrome('chromedriver', options=chrome_options)
        self._wd.get(url)# 웹페이지 가져 오기
        pass
      
    
        
    def summary(self):
        html = self._wd.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.text
        sub_title = soup.find('h2').text
        self._quit()
        return f"{title}\n\n{sub_title}"
        


    def _quit(self):
        self._wd.quit()
            