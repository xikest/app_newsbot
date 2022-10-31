from tools.file_manager.functions import FilesF
from typing import Any, Optional,List, Union
from dataclasses  import dataclass
# from tools.telegram_bot.telegram_bot import TelegramBot
from tools.time.time import Timer
import asyncio
import telegram

@dataclass
class Context:
        title:Optional[str]=None
        content:List[Any] = None
        label:Optional[str] = None
        descr:Optional[str] = None
        release_time:Optional[str] = None
        dtype:Optional[str] = None
        used:bool=False
        key:Optional[str] = None
        botChatId:Optional[str] = None

class Contents(list): 
    """
    import feedparser

    def make_content(rss_url):
      yield [Content(feed.summary, feed.title, feed.link) for feed in feedparser.parse(rss_url).entries]
          
    
    rss_url = 'https://back.nber.org/rss/releases.xml'
    
    contents = Contents()
    contents.addFromList(make_content(rss_url))
    
    contents.saveContentsDict()
    
    contents.loadContentsDict()
    """
    def __init__(self, context:Context=None):
        super().__init__()
        self.append(context)
        
    def addContext(self, context:Context=None):
        self.append(context)

    def saveContents(self, context:Context, fileName:str='contents_list'):
        sent_list=list(self.loadContents())
        sent_list.append(context)
        if len(sent_list)> 10000 : sent_list.pop()  # 버퍼 10000개로 제한
        FilesF.Pickle.save_to_pickle(sent_list, f'{fileName}')
        # return print('saved backup')

    def loadContents(self, fileName:str='contents_list'):
        try:
            # print('loaded files')
            yield from FilesF.Pickle.load_from_pickle(f'{fileName}')
        except:
            # print('loaded fail')
            yield from []
        

    
    async   def sendTo(self, token:str, delay:Union[int, float]=0) -> None:
                context:Context = self.pop()
                bot = telegram.Bot(token)
                if context not in self.loadContents():
                    self.saveContents(context=context)
                    await asyncio.sleep(Timer.sleepToRelease(context.release_time, delay))                    
                    while len(context.content) > 0:
                        if context.dtype == 'img': 
                            await   asyncio.sleep(2)
                            await   bot.send_photo(chat_id=context.botChatId, photo=context.content.pop(0))
                        else: 
                            await   asyncio.sleep(2)
                            await   bot.send_message(chat_id=context.botChatId, text=context.content.pop(0)) #'msg'
                return None
            
