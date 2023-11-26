from typing import Optional, AsyncGenerator, Generator
import imapclient
import email
from email.header import decode_header
import re
import asyncio
import datetime
import bs4
import requests
from bot.handler.contents_hanlder import Context
import os



class SrcMail:
    def __init__(self, usr: str, pid: str, mailings: Generator, chat_id: Optional[str] = None, verbose=False):
        self._usr = usr
        self._pid = pid
        self._mailings = mailings
        self._chat_id: Optional[str] = chat_id
        self.verbose = verbose

    async def generator(self) -> AsyncGenerator[Context, None]:
            for mailing in self._mailings:
                try:
                    print(f"Start getting the feed from the {mailing.sender}'s: {datetime.datetime.now()}") 
                    UIDs, raw_msg = self._get_UIDs_msg(self._usr, self._pid, mailing.box)
                    for UID in UIDs[-20:]:
                        message = email.message_from_bytes(raw_msg[UID][b'BODY[]'])
                        fr = decode_header(message.get('From'))
                        if mailing.sender in str(fr):
                            body = None
                            for part in message.walk():
                                ctype = part.get_content_type()
                                cdispo = str(part.get('Content-Disposition'))
                                body = part.get_payload(decode=True)
                                if body is not None:
                                    async for context in self._run_generator(ctype, cdispo, body, mailing):
                                        yield context
                    print(f"Finished obtaining the feed from the {mailing.sender}'s : {datetime.datetime.now()}")
                except Exception as e:
                    time_sleep = datetime.datetime.now()
                    if self.verbose:
                        print(f'Error description -> {e}')
                        print(f"Raised a feed error from the {mailing.sender}'s @{time_sleep}")
                    await asyncio.sleep(60 * 10)  #다음 반복까지 대기 시간
                    time_awake = datetime.datetime.now()
                    if self.verbose:
                        print(f"Awakened a feed error from the {mailing.sender}'s @{time_awake}")
                        print(f'Total sleep time{time_awake - time_sleep}')

                    
    async def _run_generator(self, ctype, cdispo, body, mailing):
        body = body.decode('utf-8')
        # print(f"body {body} \n")
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            urlPattern = '(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+'
            urls = re.findall(urlPattern, body)
            for url in urls:
                # print(f"{mailing.sender} plain_url before redirecion: {url}")
                url = await self._follow_url_redirects(url)
                # print(f"{mailing.sender} plain_url before filtering: {url}")
                if not mailing.url_conditions or all(condition in url for condition in mailing.url_conditions):
                    # print(f"{mailing.sender} plain_url: {url}")
                    yield Context(label = mailing.box, contents=[url], botChatId=self._chat_id, dtype='msg', enable_summary=True)


        elif ctype == 'text/html' and 'attachment' not in cdispo:
            soup = bs4.BeautifulSoup(body, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                # print(f"text/html link text : {link.text.strip()}")
                # print(f"'text/html filter condition:{mailing.filter_linktext}")
                if link.text.strip() == mailing.filter_linktext:
                    url = link.get('href')
                    url = await self._follow_url_redirects(url)
                    # print(f"{mailing.sender} html_url before filtering: {url}")
                    if not mailing.url_conditions or all(condition in url for condition in mailing.url_conditions):
                        # print(f"{mailing.sender} html_url: {url}")
                        yield Context(label = mailing.box, contents=[url], botChatId=self._chat_id, dtype='msg', enable_summary=True)

    async def _follow_url_redirects(self, url):
        # URL 유효성 검사
        if not url.startswith('http://') and not url.startswith('https://'):
            final_url = '' 
            return final_url  # 유효한 URL이 아닌 경우
        try:
            await asyncio.sleep(1)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
            response = requests.get(url, headers=headers, allow_redirects=True)
            response.raise_for_status()  # HTTP 오류가 있는지 확인
            final_url = response.url
        except requests.exceptions.RequestException as e:
            final_url = ''
            if self.verbose:
                print(f"Raised URL redirects error: {e}")
        return final_url
    
    def _get_UIDs_msg(self, usr: str, pid: str, box: str, imap: str = 'imap.naver.com'):
        imap_obj = imapclient.IMAPClient(imap, ssl=True)
        imap_obj.login(usr, pid)
        imap_obj.select_folder(box, readonly=True)
        UIDs = imap_obj.search(['ALL'])
        raw_msg = imap_obj.fetch(UIDs, ['BODY[]'])
        return UIDs, raw_msg

