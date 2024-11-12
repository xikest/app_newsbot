import telegram
import logging
from .summerizer import Summerizer
from bot.definition_obj import Context
from tools.file.filemanager import FileManager


class Handler(list):
    def __init__(self, context, token, gpt_key,  max_buffer_size=100000):
        super().__init__()
        self.max_buffer_size = max_buffer_size
        self.append(context)           
        self._token = token
        self._gpt_key = gpt_key    
            
    async def send_content(self, storage_name='app_newsbot_contents') -> None:
        try: 
            context = self.pop()
            if not context:
                return  # 컨텐츠가 없으면 아무 것도 하지 않음
            if context.link not in self._load_contents(storage_name):
                self._save_contents(context.link, storage_name)
                await self._send_msg(context)
            else:
                bot = telegram.Bot(self._token)
                await bot.send_message(chat_id="-1001673032661", text="test")
                raise ValueError
        except Exception as e: 
            logging.error(f"error send_contents: {e}")
            
    async def _send_msg(self, context:Context):
        bot = telegram.Bot(self._token)
        try:
            context = self._make_summary(context, self._gpt_key)
            logging.debug(f"context: {context}")
            if context.dtype == 'msg':
                if context.summary != "":
                    msg = f"#{context.label}\n{context.summary}\n{context.link}"
                else:    
                    msg = f"#{context.label}\n{context.link}"
                await bot.send_message(chat_id=context.bot_chat_id, text=msg)
            else:
                raise ValueError("Unsupported content type: dtype is not defined.")
        except Exception as e:
            logging.error(f"Error_send_contents: {e}")
            pass   
        
    def _save_contents(self, contents: str, storage_name):
        sent_list = list(self._load_contents(storage_name))
        sent_list.append(contents)
        if len(sent_list) > self.max_buffer_size:
            sent_list.pop(0)  # 버퍼 크기를 초과하면 가장 오래된 컨텐츠를 제거
        FileManager.save_to_pickle(sent_list, storage_name)
        
    def _load_contents(self, storage_name):
        try:
            yield from FileManager.load_from_pickle(storage_name)
        except Exception as e:
            yield from []
            
    def _make_summary(self, context: Context, gpt_key:str):
        if context.enable_translate:
            try:
                summerizer = Summerizer(api_key=gpt_key, gpt_model='gpt-4o-mini')
                context.summary = summerizer.translate_tokr(context.summary)
            except:
                pass
        return context     
        
