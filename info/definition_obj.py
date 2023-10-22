from typing import Any, Optional,List
from dataclasses import dataclass

@dataclass
class Context:
    label: Optional[str] = None
    content: List[Any] = None
    dtype: Optional[str] = None
    botChatId: Optional[str] = None

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
    exceptions:[] = None
    

@dataclass
class Mail:
    box: str
    sender: str
    filter_linktext: str
    conditions:[] = None
