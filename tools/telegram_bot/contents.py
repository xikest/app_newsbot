from tools.file_manager.functions import FilesF
from typing import Any, Optional,List, Union
from dataclasses  import dataclass
# from tools.telegram_bot.telegram_bot import TelegramBot
from tools.time.time import Timer
import asyncio
import telegram
import re
from nltk import sent_tokenize

from tools.translate import Kakao, Papago

from .summary import Wsj, Iea

@dataclass
class Context:
        label:Optional[str] = None
        content:List[Any] = None
        dtype:Optional[str] = None
        botChatId:Optional[str] = None
        
        summary:List[Any] = None
        enable_translate:bool = False
        tokenize:bool = False
        enable_summary:bool = False
        

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
                # print('send start')
                if context not in self.loadContents():
                    self.saveContents(context=context)
                    # print('no in loading')
                    #await asyncio.sleep(Timer.sleepToRelease(context.release_time, delay))         
                    try:           
                        # context = self.makeSummary(context)  # 요약본 생성
                        while len(context.content) > 0:   
                            # print('loop start')   
                            # print(context)            
                            if context.dtype == 'img': 
                                await asyncio.sleep(5)
                                await bot.send_photo(chat_id=context.botChatId, photo=context.content.pop(0))
                                
                            elif context.dtype == 'msg':
                                if context.enable_translate == True:
                                    msg = f"#{context.label}\n{await self.translate(context.summary.pop(0))}\n\n{context.content.pop(0)}"
                                    # print(f'translate : {msg}')
                                elif context.enable_translate == False:
                                    msg = f"#{context.label}\n\n{context.content.pop(0)}"
                                # print(f'msg : {msg}')
                                await asyncio.sleep(5)
                                await bot.send_message(chat_id=context.botChatId, text=msg) #'msg'
                            else: raise Exception("dtype이 정의되지 않았습니다.")
                    except:pass
                return None

     

     
            
    async def translate(self, paragraph:str) -> str:
       
        # if tokenize == True:
        #     tokenized_sentences = sent_tokenize(paragraph)  #문장 단위로 쪼개기
        #     try: sentences = " ".join([await Papago('en').translate(sentence) for sentence in tokenized_sentences])
        #     except: sentences = " ".join([await Kakao('en').translate(sentence) for sentence in tokenized_sentences])
            
            
        # else:        
        #     paragraph = self.paragraphTrimming(paragraph)  # 불용어 제거   
        #     try: sentences = await Papago('en').translate(paragraph)
        #     except: sentences = await Kakao('en').translate(paragraph)
        paragraph = self.paragraphTrimming(paragraph)  # 불용어 제거  
        try: sentences = await Papago('en').translate(paragraph) 
        except Exception as e:
            print(f"translate err {e}")
            sentences = ""
            # sentences = await Kakao('en').translate(paragraph)
        return sentences
    
    def paragraphTrimming(self, paragraph):
        regexes = [
            r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', #http 주소 제거
            # r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', #http 아닌 웹주소 제거
            'oott',
            'OOTT'
            ]  
        
        for regex in regexes: paragraph = re.sub(regex,"",paragraph) # 필요없는 문장 제거
        return paragraph
    
    def makeSummary(self, context:Context):
        if context.enable_summary==True:

            if context.label == 'WSJ_NEWS':   #WSJ 기사 요약
                context.summary = [Wsj().summary(url= content) for content in context.content]
                context.enable_translate=True # 번역할 것인지 
                # context.tokenize=True  #텍스트 토큰화 실행


            elif context.label == 'IEA':
                context.summary = [Iea().summary(url = content) for content in context.content]
                context.enable_translate=True # 번역할 것인지 
                # context.tokenize=True  #텍스트 토큰화 실행
                
            # elif context.label == 'WHALE_WISDOM':
                
            #     context.summary = [Wisdom().summary(url = content) for content in context.content]
            #     context.enable_translate=False # 번역할 것인지 
                
                
        
        
        # print(f'summariziong: {context}')    
        return context 
