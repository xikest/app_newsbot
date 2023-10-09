import asyncio
import telegram
from info.definition_obj import Context
from bot.handler.function_handler import FunctionHandler

class ContentsHandler(list):
    def __init__(self, context: Context = None, max_buffer_size=10000):
        super().__init__()
        self.append(context)
        self.max_buffer_size = max_buffer_size

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
            print("sendTo",token, type(token))
            bot = telegram.Bot(token)
            print("made bot")
            if context not in self.loadContents():
                self.saveContents(context=context)
                await self._sendContents(context, bot)
        except Exception as e: 
            print("errr",e)

    async def _sendContents(self, context: Context, bot: telegram.Bot):
        try:
            while context.content:
                if context.dtype == 'img':
                    await asyncio.sleep(10)
                    await bot.send_photo(chat_id=context.botChatId, photo=context.content.pop(0))
                elif context.dtype == 'msg':
                    msg = f"{context.content.pop(0)}"
                    await asyncio.sleep(10)
                    await bot.send_message(chat_id=context.botChatId, text=msg)
                else:
                    raise ValueError("Unsupported content type: dtype is not defined.")
        except Exception as e:
            print(f"Error sending contents: {e}")




# import asyncio
# import telegram
#
# from bot.handler.function_handler import FunctionHandler
# from info.definition_obj import Context
#
# class ContentsHandler(list):
#     def __init__(self, context:Context=None):
#         super().__init__()
#         self.append(context)
#
#     def addContext(self, context:Context=None):
#         self.append(context)
#
#     def saveContents(self, context:Context, fileName:str='contents_list'):
#         sent_list=list(self.loadContents())
#         sent_list.append(context)
#         if len(sent_list)> 10000 : sent_list.pop()  # 버퍼 10000개로 제한
#         FunctionHandler.Pickle.save_to_pickle(sent_list, f'{fileName}')
#         # return print('saved backup')
#
#     def loadContents(self, fileName:str='contents_list'):
#         try:
#             # print('loaded files')
#             yield from FunctionHandler.Pickle.load_from_pickle(f'{fileName}')
#         except:
#             # print('loaded fail')
#             yield from []
#
#     async   def sendTo(self, token:str) -> None:
#                 context:Context = self.pop()
#                 bot = telegram.Bot(token)
#                 if context not in self.loadContents():
#                     self.saveContents(context=context)
#                     try:
#                         while len(context.content) > 0:
#                             if context.dtype == 'img':
#                                 await asyncio.sleep(5)
#                                 await bot.send_photo(chat_id=context.botChatId, photo=context.content.pop(0))
#                             elif context.dtype == 'msg':
#                                 msg = f"{context.content.pop(0)}"
#                                 await asyncio.sleep(5)
#                                 await bot.send_message(chat_id=context.botChatId, text=msg) #'msg'
#                             else: raise Exception("dtype이 정의되지 않았습니다.")
#                     except:pass
#                 return None
#
