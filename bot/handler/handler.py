import telegram
import logging
import os 
import hashlib
from datetime import datetime
from .assistant import Assistant
from bot.definition_obj import Context
from tools.file.filemanager import FileManager
from tools.gcp.firestoremanager import FirestoreManager

def get_today_date():
    today = datetime.today()
    return today.strftime('%Y-%m-%d')


class Handler:
    def __init__(self, context: Context, token: str, gpt_key: str, firestore_auth:str):
        self.context = context  
        # self.max_buffer_size = max_buffer_size          
        self._token = token
        self._gpt_key = gpt_key    
        self.firestore = FirestoreManager(firestore_auth)
            
    async def send_content(self, storage_name) -> None:
        def url_to_doc_key_sha256(url: str) -> str:
            return hashlib.sha256(url.encode('utf-8')).hexdigest()
        
        doc_key = url_to_doc_key_sha256(self.context.link)
        try:
            if not self.firestore.is_doc_key_exist(doc_key=doc_key, collection_name = storage_name):
                self.firestore.save_db(doc_key=doc_key, 
                                       data_dict={"title": self.context.title, "date":get_today_date(), "link":self.context.link}, 
                                       collection_name= storage_name)
                await self._send_msg(self.context)
        except Exception as e:
            logging.error(f"[send_content] Transmission error: {e}")

            
    async def _send_msg(self, context: Context):
        bot = telegram.Bot(self._token)
        try:
            context = self._processing_with_assistant(context)
            message = f"#{context.label}\n{context.title or ''}\n{context.link}"
            await bot.send_message(chat_id=context.bot_chat_id, text=message)
        except Exception as e:
            logging.error(f"[send_msg] Message sending error: {e}")
                
    def _processing_with_assistant(self, context: Context) -> Context:
        if context.enable_translate:
            try:
                gpt_model = os.getenv("GPT_MODEL", "gemini-2.0-flash-exp")
                assistant = Assistant(api_key=self._gpt_key, gpt_model = gpt_model)
                context.title = assistant.translate_tokr(context.title)
            except Exception as e:
                logging.error(f"[make_summary] Summary generation error: {e}")
        return context
    
