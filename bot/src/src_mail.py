from typing import Optional, AsyncGenerator, Generator
import imapclient
import email
from email.header import decode_header
import re
import asyncio
import datetime
import bs4
import requests
# import pyshorteners
from bot.handler.contents_hanlder import Context

class SrcMail:
    def __init__(self, usr: str, pid: str, mailings: Generator, chat_id: Optional[str] = None):
        self._usr = usr
        self._pid = pid
        self._mailings = mailings
        self._chat_id: Optional[str] = chat_id

    async def generator(self) -> AsyncGenerator[Context, None]:
            for mailing in self._mailings:
                try:
                    print(f'start get feed from mail of "{mailing.sender}": {datetime.datetime.now()}') 
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
                    print(f'finish to get feed from mail of {mailing.sender}: {datetime.datetime.now()}')
                except Exception as e:
                    time_sleep = datetime.datetime.now()
                    print(f'raised feed error from mail of {mailing.sender} @{time_sleep}')
                    print(f'error description -> {e}')
                    await asyncio.sleep(30 * 60)
                    time_awake = datetime.datetime.now()
                    print(f'awaked feed error of mail of {mailing.sender} @{time_awake}')
                    print(f'total sleep time{time_awake - time_sleep}')

                    

    async def _run_generator(self, ctype, cdispo, body, mailing):
        body = body.decode('utf-8')
        # print(f"body {body} \n")
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            urlPattern = '(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+'
            urls = re.findall(urlPattern, body)
            for url in urls:
                url = await self._follow_url_redirects(url)
                print(f"{mailing.sender} plain_url before filtering: {url}")
                if not mailing.conditions or all(condition in url for condition in mailing.conditions):
                    print(f"{mailing.sender} plain_url: {url}")
                    yield Context(content=[url], botChatId=self._chat_id, dtype='msg')

        elif ctype == 'text/html' and 'attachment' not in cdispo:
            soup = bs4.BeautifulSoup(body, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                if link.text.strip() == "Read More":
                    url = link.get('href')
                    url = await self._follow_url_redirects(url)
                    if not mailing.conditions or all(condition in url for condition in mailing.conditions):
                        print(f"{mailing.sender} html_url: {url}")
                        yield Context(content=[url], botChatId=self._chat_id, dtype='msg')
                        

    async def _follow_url_redirects(self, url):
        # URL 유효성 검사
        if not url.startswith('http://') and not url.startswith('https://'):
            final_url = '' 
            return final_url  # 유효한 URL이 아닌 경우

        try:
            response = requests.get(url, allow_redirects=True)
            response.raise_for_status()  # HTTP 오류가 있는지 확인
            final_url = response.url
        except requests.exceptions.RequestException as e:
            final_url = ''
            print(f"url_redirects_error: {e}")

        return final_url
    
    def _get_UIDs_msg(self, usr: str, pid: str, box: str, imap: str = 'imap.naver.com'):
        imap_obj = imapclient.IMAPClient(imap, ssl=True)
        imap_obj.login(usr, pid)
        imap_obj.select_folder(box, readonly=True)
        UIDs = imap_obj.search(['ALL'])
        raw_msg = imap_obj.fetch(UIDs, ['BODY[]'])
        return UIDs, raw_msg

