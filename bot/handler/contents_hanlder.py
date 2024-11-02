import telegram
import asyncio
import pickle
import logging
import gzip
from pathlib import Path
from info.definition_obj import Context
from bot.handler.sentimentmanager import SentimentManager as SentiGPT
from info.sender import Sender

class ContentsHandler(list):
    def __init__(self, context: Context = None, max_buffer_size=100000):
        super().__init__()
        self.max_buffer_size = max_buffer_size
        self.append(context)           
        self._token = Sender().get_token()
        self._gpt_key = Sender().get_gptkey()    
            
    async def send_contents(self, storage_name='app_newsbot_contents') -> None:
        async def _send_content(context: Context):
            bot = telegram.Bot(self._token)
            try:
                context = self._make_summary(context, self._gpt_key)
                logging.debug(f"context: {context}")
                if context.dtype == 'msg':
                    contents = ""
                    while context.contents: 
                        contents += context.contents.pop(0)
                    if context.summary != "":
                        msg = f"#{context.label}\n{context.summary}\n{contents}"
                    else:    
                        msg = f"#{context.label}\n{contents}"
                    await bot.send_message(chat_id=context.botChatId, text=msg)
                    await asyncio.sleep(1)
                else:
                    raise ValueError("Unsupported content type: dtype is not defined.")
            except Exception as e:
                logging.error(f"Error_send_contents: {e}")
                pass
        
        try: 
            context = self.pop()
            if not context:
                return  # 컨텐츠가 없으면 아무 것도 하지 않음
            if context.contents[0] not in self._load_contents(storage_name):
                self._save_contents(context.contents[0], storage_name)
                await _send_content(context)
        except Exception as e: 
            logging.error(f"error send_contents: {e}")
            
        
    def _save_contents(self, contents: str, storage_name):
        sent_list = list(self._load_contents(storage_name))
        sent_list.append(contents)
        if len(sent_list) > self.max_buffer_size:
            sent_list.pop(0)  # 버퍼 크기를 초과하면 가장 오래된 컨텐츠를 제거
        self.save_to_pickle(sent_list, storage_name)
    def _load_contents(self, storage_name):
        
        try:
            yield from self.load_from_pickle(storage_name)
        except Exception as e:
            yield from []
            
    
    def _make_summary(self, context:Context, gpt_key:str):
        if context.enable_translate:
            try:
                sgpt = SentiGPT(api_key=gpt_key, gpt_model='gpt-4o-mini')
                context.summary = sgpt.translate_tokr(context.summary)
            except:
                pass
        return context     
        

    def save_to_pickle(self, data, storage_name, data_path: Path = Path.cwd()):
        with gzip.open(f"{data_path}/{storage_name}.pickle", 'wb') as f:
            pickle.dump(data, f)

    def load_from_pickle(self, storage_name, data_path: Path = Path.cwd()):
        with gzip.open(f"{data_path}/{storage_name}.pickle", 'rb') as f:
            return pickle.load(f)
