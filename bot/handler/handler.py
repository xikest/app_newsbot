import telegram
import logging
from .summerizer import Summerizer
from bot.definition_obj import Context
from tools.file.filemanager import FileManager

class Handler:
    def __init__(self, context: Context, token: str, gpt_key: str, max_buffer_size: int = 100000):
        self.context = context  
        self.max_buffer_size = max_buffer_size          
        self._token = token
        self._gpt_key = gpt_key    
            
    async def send_content(self, storage_name='app_newsbot_contents') -> None:
        try:
            if self.context and not self._content_exists(self.context.link, storage_name):
                self._save_contents(self.context.link, storage_name)
                await self._send_msg(self.context)
        except Exception as e:
            logging.error(f"[send_content] Transmission error: {e}")

            
    async def _send_msg(self, context: Context):
        bot = telegram.Bot(self._token)
        try:
            context = self._make_summary(context)
            message = f"#{context.label}\n{context.summary or ''}\n{context.link}"
            await bot.send_message(chat_id=context.bot_chat_id, text=message)
        except Exception as e:
            logging.error(f"[send_msg] Message sending error: {e}")

            
    def _content_exists(self, link: str, storage_name: str) -> bool:
        return link in self._load_contents_as_list(storage_name)
    
    def _save_contents(self, link: str, storage_name: str):
        contents = self._load_contents_as_list(storage_name)
        contents.append(link)
        if len(contents) > self.max_buffer_size:
            contents.pop(0)  #When the buffer exceeds its capacity, the oldest item will be removed
        FileManager.save_to_pickle(contents, storage_name)

    def _load_contents_as_list(self, storage_name: str) -> list:
        try:
            return list(FileManager.load_from_pickle(storage_name))
        except Exception as e:
            logging.error(f"[load_contents_as_list] Error loading from {storage_name}: {e}")
            return []
                
    def _make_summary(self, context: Context) -> Context:
        if context.enable_translate:
            try:
                summerizer = Summerizer(api_key=self._gpt_key, gpt_model='gemini-1.5-flash')
                context.summary = summerizer.translate_tokr(context.summary)
            except Exception as e:
                logging.error(f"[make_summary] Summary generation error: {e}")
        return context