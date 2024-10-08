from typing import Any, Optional,List
from dataclasses import dataclass

@dataclass
class Context:
    label: Optional[str] = None
    contents: List[Any] = None
    dtype: Optional[str] = None
    botChatId: Optional[str] = None
    enable_summary:bool = False
    enable_translate:bool = False
    summary:str =""

@dataclass
class News:
    name: str
    src: str
    url: str
    attr_key: Optional[str] = None
    selector: Optional[str] = None
    prefix: Optional[str] = None
    startswith: str = 'http'
    class_key: Optional[str] = None
    exceptions:list = None
    enable_translate:bool = False
    url_original:bool=False
    

@dataclass
class Mail:
    box: str
    sender: str
    filter_linktext: str = ""
    url_conditions:list = None
