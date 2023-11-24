import asyncio
import telegram
from info.definition_obj import Context
from bot.handler.function_handler import FunctionHandler
import os
from .summary import WSJ_Scraper
from .sentimentmanager import SentimentManager as SentiGPT
class ContentsHandler(list):
    def __init__(self, context: Context = None, max_buffer_size=10000):
        super().__init__()
        self.append(context)
        self.max_buffer_size = max_buffer_size
        self.gpt_api_key = os.environ.get("GPT_API_KEY")
        self.bot_token = os.environ.get("BOT_TOKEN")
    def addContext(self, context: Context = None):
        self.append(context)
    def saveContents(self, context: Context, fileName: str = 'contents_list'):
        sent_list = list(self.loadContents())
        sent_list.append(context)
        if len(sent_list) > self.max_buffer_size:
            sent_list.pop(0)  # 버퍼 크기를 초과하면 가장 오래된 컨텐츠를 제거
        FunctionHandler.Pickle.save_to_pickle(sent_list, fileName)
    def loadContents(self, fileName: str = 'contents_list'):
        try:
            yield from FunctionHandler.Pickle.load_from_pickle(fileName)
        except FileNotFoundError:
            yield from []
    async def sendTo(self, token: str) -> None:
        try: 
            context = self.pop()
            if not context:
                return  # 컨텐츠가 없으면 아무 것도 하지 않음

            if context not in self.loadContents():
                self.saveContents(context=context)
                await self._sendContents(context)
        except Exception as e: 
            print("error sendTo",e)
    async def _sendContents(self, context: Context):

        bot = telegram.Bot(self.bot_token)
        try:
            while context.contents:
                if context.dtype == 'msg':
                    # context = self.makeSummary(context)
                    if context.summary:
                        msg = f"#{context.label}\n {context.summary.pop(0)}\n\n{context.contents.pop(0)}"
                    else:
                        msg = f"#{context.label}\n\n{context.summary.pop(0)}"
                    await asyncio.sleep(10)
                    await bot.send_message(chat_id=context.botChatId, text=msg)
                else:
                    raise ValueError("Unsupported content type: dtype is not defined.")
        except Exception as e:
            print(f"Error _sendContents: {e}")
            pass
    #
    def makeSummary(self, context:Context):
        if context.enable_summary:
            if context.label == 'WSJ_NEWS':
                sgpt = SentiGPT(api_key=self.gpt_api_key)
                text_list = []
                for content in context.contents:
                    text = WSJ_Scraper().summary(url=content)
                    text = sgpt.translate_tokr(sentence=text)
                    text_list.append(text)
                context.summary = text_list

        else:
            context.summary = context.contents
            context.enable_translate = False  # 번역할 것인지
        return context