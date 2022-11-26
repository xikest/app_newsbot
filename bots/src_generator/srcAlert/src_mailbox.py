from typing import Optional
from tools.telegram_bot.contents import Context
import imapclient
import email
from email.header import decode_header
import re
from tools.telegram_bot.contents import Context



class SrcMailBox:
    def __init__(self, usr:str, pid:str, box:str, sender:str, ChatId:str=None):
        self._usr = usr
        self._pid = pid
        self._box = box
        self._sender = sender
        self._ChatId:Optional[str]=ChatId

    def generator(self)-> Context:
        UIDs, raw_msg = self._get_UIDs_msg( self._usr, self._pid, self._box)
        for UID in UIDs[-20:]:  # 최근 20개만 읽음
            message = email.message_from_bytes(raw_msg[UID][b'BODY[]'])
            fr = decode_header(message.get('From'))
            if  self._sender in str(fr):
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
                # asyncio.sleep(1)
                yield Context(content=[url], botChatId=self._ChatId)
                
    def _get_UIDs_msg(self, usr:str, pid:str, box:str, imap:str ='imap.naver.com'):
        imap_obj = imapclient.IMAPClient(imap, ssl=True)
        imap_obj.login(usr, pid)
        imap_obj.select_folder(box, readonly=True)
        UIDs = imap_obj.search(['ALL'])
        raw_msg = imap_obj.fetch(UIDs, ['BODY[]'])
        return UIDs, raw_msg