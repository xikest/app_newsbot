import telegram
import asyncio
import pickle
import gzip
from pathlib import Path
from info.definition_obj import Context
from .sentimentmanager import SentimentManager as SentiGPT

class ContentsHandler(list):
    def __init__(self, context: Context = None, max_buffer_size=100000):
        super().__init__()
        self.append(context)
        self.max_buffer_size = max_buffer_size

    async def send_to(self, token: str, gpt:str) -> None:
        try: 
            context = self.pop()
            if not context:
                return  # 컨텐츠가 없으면 아무 것도 하지 않음
            if context not in self._load_contents():
                self._save_contents(context=context)
                await self._send_contents(context, token, gpt)
        except Exception as e: 
            print(f"error sendTo: {e}")
            
    async def _send_contents(self, context: Context, bot_token: str, gpt_key:str):
        # print(f"bot token: {self.bot_token}")
        bot = telegram.Bot(bot_token)
        try:
            context = self._make_summary(context, gpt_key)
            # print(f"context: {context}")
            if context.dtype == 'msg':
                contents = ""
                while context.contents: 
                    contents += context.contents.pop(0)
                if context.summary is not "":
                    msg = f"#{context.label}\n{context.summary}\n{contents}"
                else:    
                    msg = f"#{context.label}\n{contents}"
                await bot.send_message(chat_id=context.botChatId, text=msg)
                await asyncio.sleep(1)
            else:
                raise ValueError("Unsupported content type: dtype is not defined.")
        except Exception as e:
            print(f"Error_send_contents: {e}")
            pass
        
    def _save_contents(self, context: Context, file_name: str = 'app_newsbot_contents'):
        sent_list = list(self._load_contents())
        sent_list.append(context)
        if len(sent_list) > self.max_buffer_size:
            sent_list.pop(0)  # 버퍼 크기를 초과하면 가장 오래된 컨텐츠를 제거
        self.save_to_pickle(sent_list, file_name)
        
    def _load_contents(self, file_name: str = 'app_newsbot_contents'):
        try:
            yield from self.load_from_pickle(file_name)
        except FileNotFoundError:
            yield from []
            
    
    def _make_summary(self, context:Context, gpt_key:str):
        if context.enable_translate:
            try:
                sgpt = SentiGPT(api_key=gpt_key, gpt_model='gpt-4o-mini')
                context.summary = sgpt.translate_tokr(context.summary)
            except:
                pass
        return context     
        

    def save_to_pickle(self, data, file_name, data_path: Path = Path.cwd().parent):
        with gzip.open(f"{data_path}/{file_name}.pickle", 'wb') as f:
            pickle.dump(data, f)

    def load_from_pickle(self, file_name, data_path: Path = Path.cwd().parent):
        with gzip.open(f"{data_path}/{file_name}.pickle", 'rb') as f:
            return pickle.load(f)
