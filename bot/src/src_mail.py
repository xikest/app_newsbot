from typing import Optional, Generator
import imapclient
import email
from email.header import decode_header
import re
import asyncio
import datetime
import bs4  # BeautifulSoup 라이브러리 추가
import pyshorteners as ps
from bot.handler.contents_hanlder import Context

class SrcMail:
    def __init__(self, usr: str, pid: str, mailings: Generator, chat_id: Optional[str] = None):
        self._usr = usr
        self._pid = pid
        self._mailings = mailings
        self._chat_id: Optional[str] = chat_id

    async def generator(self) -> Context:
        urlPattern = '(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+'
        try:
            for mailing in self._mailings:
                UIDs, raw_msg = self._get_UIDs_msg(self._usr, self._pid, mailing.box)
                for UID in UIDs[-20:]:  # 최근 20개만 읽음
                    message = email.message_from_bytes(raw_msg[UID][b'BODY[]'])
                    fr = decode_header(message.get('From'))
                    if mailing.sender in str(fr):
                        body = None
                        for part in message.walk():
                            ctype = part.get_content_type()
                            cdispo = str(part.get('Content-Disposition'))
                            
                            sh = ps.Shortener()
                            if ctype == 'text/plain' and 'attachment' not in cdispo:
                                body = part.get_payload(decode=True)  # decode
                                if body is not None:
                                    body = body.decode('utf-8')
                                    
                                    urls = re.findall(urlPattern, body)
                                    for url in urls:
                                        if not mailing.conditions or all(condition in url for condition in mailing.conditions):
                                            url = sh.post.short(url)
                                             # print(f"링크 주소: {url}")
                                            await asyncio.sleep(10)
                                            yield Context(label=f'{mailing.box}', content=[url], botChatId=self._chat_id, dtype='msg')

                                
                            elif ctype == 'text/html' and 'attachment' not in cdispo:
                                body = part.get_payload(decode=True)  # HTML 본문을 읽어옴
                                if body is not None:
                                    body = body.decode('utf-8')
                                    
                                    # BeautifulSoup을 사용하여 HTML 본문을 파싱
                                    soup = bs4.BeautifulSoup(body, 'html.parser')
                                    links = soup.find_all('a')
                                    for link in links:
                                        if link.text.strip() == "Read More":
                                            url = link.get('href')
                                            url = sh.post.short(url)
                                             # print(f"링크 주소: {url}")
                                            await asyncio.sleep(10)
                                            yield Context(label=f'{mailing.box}', content=[url], botChatId=self._chat_id, dtype='msg')


            print(f'mail_src_fin: {datetime.datetime.now()}\n')
        except Exception as e:
            print(f'mail_src_err -> sleep: {datetime.datetime.now()}')
            print(f'err -> {e}')
            await asyncio.sleep(30 * 60)
            print(f'mail_src_err -> awake: {datetime.datetime.now()}\n')

    def _get_UIDs_msg(self, usr: str, pid: str, box: str, imap: str = 'imap.naver.com'):
        imap_obj = imapclient.IMAPClient(imap, ssl=True)
        imap_obj.login(usr, pid)
        imap_obj.select_folder(box, readonly=True)
        UIDs = imap_obj.search(['ALL'])
        raw_msg = imap_obj.fetch(UIDs, ['BODY[]'])
        return UIDs, raw_msg
