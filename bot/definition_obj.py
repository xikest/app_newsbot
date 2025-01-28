from dataclasses import dataclass

@dataclass
class Context:
    label: str = None
    link:str = None
    dtype: str = None
    bot_chat_id: str = None
    enable_summary:bool = False
    enable_translate:bool = False
    title:str = None
    trx_mp3:bool=False