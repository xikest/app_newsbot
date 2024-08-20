import asyncio
import telegram
import pickle
import gzip
from pathlib import Path
from info.definition_obj import Context
# from .summary import Summary_scraper
from .sentimentmanager import SentimentManager as SentiGPT

class ContentsHandler(list):
    def __init__(self, context: Context = None, max_buffer_size=100000):
        super().__init__()
        self.append(context)
        self.max_buffer_size = max_buffer_size


    async def sendTo(self, token: str, gpt:str) -> None:
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
            while context.summary:
                if context.dtype == 'msg':
                    msg = f"#{context.label}\n{context.summary.pop(0)}"
                    await bot.send_message(chat_id=context.botChatId, text=msg)
                else:
                    raise ValueError("Unsupported content type: dtype is not defined.")
        except Exception as e:
            print(f"Error _sendContents: {e}")
            pass
        
    def _save_contents(self, context: Context, fileName: str = 'app_newsbot_contents'):
        sent_list = list(self._load_contents())
        sent_list.append(context)
        if len(sent_list) > self.max_buffer_size:
            sent_list.pop(0)  # 버퍼 크기를 초과하면 가장 오래된 컨텐츠를 제거
        self.save_to_pickle(sent_list, fileName)
        
    def _load_contents(self, fileName: str = 'app_newsbot_contents'):
        try:
            yield from self.load_from_pickle(fileName)
        except FileNotFoundError:
            yield from []
            
    
    def _make_summary(self, context:Context, gpt_key:str):
        if context.enable_translate:
            try:
                sgpt = SentiGPT(api_key=gpt_key, gpt_model='gpt-4o-mini')
                context.label = sgpt.translate_tokr(context.label)
            except:
                pass
            
        # if context.enable_summary:
        #     if context.label == 'WSJ_NEWS':
        #         sgpt = SentiGPT(api_key=gpt_key)
        #         summary = []
        #         for content in context.contents:
        #             print("content")
        #             print(content)
        #             text = Summary_scraper().wsj_summary(url=content)
        #             text = sgpt.translate_tokr(sentence=text)
        #             summary.append(f"{text}\n{content}")
        #         context.summary = summary
        #
        #     else:
        #         sgpt = SentiGPT(api_key=gpt_key)
        #         summary = []
        #         for content in context.contents:
        #             text = Summary_scraper().summary(url=content)
        #             text = sgpt.translate_tokr(sentence=text)
        #             summary.append(f"{text}\n{content}")
        #         context.summary = summary
        # else:
        #     context.summary = context.contents
        # return context

        context.summary = context.contents
        return context

    def save_to_pickle(self, data, file_name, data_path: Path = Path.cwd().parent):
        with gzip.open(f"{data_path}/{file_name}.pickle", 'wb') as f:
            pickle.dump(data, f)

    def load_from_pickle(self, file_name, data_path: Path = Path.cwd().parent):
        with gzip.open(f"{data_path}/{file_name}.pickle", 'rb') as f:
            return pickle.load(f)
