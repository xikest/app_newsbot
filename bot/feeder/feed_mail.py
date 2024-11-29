from typing import Optional, AsyncGenerator, Generator
import imapclient
import email
from email.header import decode_header
import re
import asyncio
import datetime
import logging
import bs4
import requests
import os
from bot.definition_obj import Context


class MAIL:
    def __init__(self, chat_id:str, verbose:bool=False, *args, **kwargs):
        
        # self.user = os.getenv("USER")
        self.user = 'taest12'
        self.pid = os.getenv("PID") 
        self.chat_id = chat_id
        self.verbose = verbose
        self.box_name:str = kwargs.get("box_name", None)
        self.sender:str = kwargs.get("sender", None)
        self.redirection_url:str = kwargs.get("redirection_url", None)
        self.enable_translate:bool = kwargs.get("enable_translate", False)
        self.url_conditions:list = kwargs.get("url_conditions", [])
        self.filter_linktext:str = kwargs.get("filter_linktext", None)


        

    async def generator(self) -> AsyncGenerator[Context, None]:
            def _get_UIDs_msg( user: str, pid: str, mail_box: str, imap: str = 'imap.naver.com'):
                imap_obj = imapclient.IMAPClient(imap, ssl=True)
                imap_obj.login(user, pid)
                imap_obj.select_folder(mail_box, readonly=True)
                UIDs = imap_obj.search(['ALL'])
                raw_msg = imap_obj.fetch(UIDs, ['BODY[]'])
                return UIDs, raw_msg


            try:
                logging.info(f"Start getting the feed from the {self.sender}'s") 
                UIDs, raw_msg = _get_UIDs_msg(self.user, self.pid, self.box_name)
                for UID in UIDs[-20:]:
                    message = email.message_from_bytes(raw_msg[UID][b'BODY[]'])
                    fr = decode_header(message.get('From'))
                    if self.sender in str(fr):
                        for part in message.walk():
                            ctype = part.get_content_type()
                            cdispo = str(part.get('Content-Disposition'))
                            async for context in self._run_generator(ctype, cdispo, part):
                                yield context
                logging.info(f"Finished obtaining the feed from the {self.sender}'s")
            except Exception as e:
                if self.verbose:
                    logging.error(f'Error description -> {e}')
                    
    async def _run_generator(self, ctype, cdispo, part):
        def follow_url_redirects(self, url):
            # URL 유효성 검사
            if not url.startswith('http://') and not url.startswith('https://'):
                final_url = ''
            if self.redirection_url:
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
                    response = requests.get(url, headers=headers, allow_redirects=True)
                    response.raise_for_status() 
                    final_url = response.url
                except requests.exceptions.RequestException as e:
                    final_url = response.url
                    if self.verbose:
                        logging.error(f"Raised URL redirects error: {e}")
            else: 
                final_url = url
            return final_url
        
        # print(f"body {body} \n")
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)
            body = body.decode('utf-8')
            urlPattern = '(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+'
            urls = re.findall(urlPattern, body)
            for url in urls:
                # logging.INFO(f"{self.sender} plain_url before redirecion: {url}")
                url = follow_url_redirects(url)
                # logging.INFO(f"{self.sender} plain_url before filtering: {url}")
                if not self.url_conditions or all(condition in url for condition in self.url_conditions):
                    logging.INFO(f"{self.sender} plain_url: {url}")
                    # yield Context(label=f'{self.box_name}', summary=title, link=url, bot_chat_id=self.chat_id, dtype='msg')
                    yield Context(label=f'{self.box_name}', link=url, bot_chat_id=self.chat_id, dtype='msg')
                                        
        elif ctype == 'text/html' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)
            soup = bs4.BeautifulSoup(body, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                # logging.INFO(f"text/html link text : {link.text.strip()}")
                # logging.INFO(f"'text/html filter condition:{self.filter_linktext}")
                if link.text.strip() == self.filter_linktext:
                    url = link.get('href')
                    url = await follow_url_redirects(url)
                    # logging.INFO(f"{self.sender} html_url before filtering: {url}")
                    if not self.url_conditions or all(condition in url for condition in self.url_conditions):
                        logging.INFO(f"{self.sender} html_url: {url}")
                        yield Context(label=f'{self.box_name}', link=url, bot_chat_id=self.chat_id, dtype='msg')

        elif ctype == 'multipart/alternative' and 'attachment' not in cdispo:
                for subpart in part.get_payload():
                    sub_ctype = subpart.get_content_type()
                    # sub_cdispo = str(subpart.get('Content-Disposition'))
                    if sub_ctype == 'text/plain' or sub_ctype == 'text/html':
                        body = subpart.get_payload(decode=True)
                        soup = bs4.BeautifulSoup(body, 'html.parser')
                        links = soup.find_all('a')
                        for link in links:
                            # print(f"text/html link text : {link.text.strip()}")
                            # print(f"'text/html filter condition:{mailing.filter_linktext}")
                            if link.text.strip() == self.filter_linktext:
                                url = link.get('href')
                                url = await follow_url_redirects(url)
                                # print(f"{mailing.sender} html_url before filtering: {url}")
                                if not self.url_conditions or all(condition in url for condition in self.url_conditions):
                                    logging.INFO(f"{self.sender} html_url: {url}")
                                    yield Context(label=f'{self.box_name}', link=url, bot_chat_id=self.chat_id, dtype='msg')


    
