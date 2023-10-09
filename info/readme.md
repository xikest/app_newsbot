# Feeder, Sender 클래스 퀵 가이드

## Feeder 클래스 퀵 가이드
`Feeder` 클래스는 여러 웹 소스 및 이메일 정보를 관리하고, 해당 정보를 가져오는 데 사용되는 클래스입니다.

### 클래스 생성 및 초기화

`Feeder` 클래스의 인스턴스를 생성합니다.
```python
feeder = Feeder()
```

### 메일 정보 및 웹 소스 정보

#### 메일 정보
`feeder_mail_info` 속성은 이메일 정보를 딕셔너리 형태로 저장합니다.

```python
{
    'usr': 'mail info',  # 이메일 사용자명
    'pid': 'mail info',  # 이메일 비밀번호
}
```
#### 웹 소스 정보
`feeder_web_source` 속성은 다양한 웹 소스 정보를 딕셔너리로 저장합니다. <br>
각 웹 소스는 `News` 객체 및 `Mail` 객체의 리스트로 표현됩니다.

```python
{
    'news_chatid': '[telegram chat ID]',  # 뉴스 채팅 ID
    'news': [
        News(name='name', src='web', url='url', attr_key='parsing'),  # 웹 소스 정보
    ],
    'rss_articles_chatid': '[telegram chat ID]',  # RSS 뉴스 채팅 ID
    'rss_articles': [
        News(name='name', src='rss', url='url'),  # RSS 뉴스 소스 정보
    ],
    'mail_chatid': '[telegram chat ID]',  # 메일 채팅 ID
    'mail': [
        Mail(box='mailbox', sender='sender', conditions=['parsing1', 'parsing2']),  # 이메일 정보
    ]
}
```

#### 클래스 메서드
> `get_keylist(source_category: str = 'news') -> list`
소스 카테고리에 해당하는 키 목록을 반환합니다.
- source_category: 반환할 카테고리 (기본값은 'news')
```python
feeder = Feeder()
keylist = feeder.get_keylist(source_category='news')  # 'news' 카테고리의 소스 키 목록을 반환합니다.
```
> `get_feeds(source: str) -> Generator`
특정 소스에 대한 정보를 생성기로 반환합니다.
- `source`: 정보를 가져올 소스 키
```python
feeder = Feeder()
news_feeds = feeder.get_feeds(source='news')  # 'news' 소스의 정보를 생성기로 반환합니다.
for feed in news_feeds:
    # feed를 처리하는 코드 작성
```

> `get_chatId(source: str) -> str`
특정 소스의 채팅 ID를 반환합니다.
- `source`: 채팅 ID를 가져올 소스 키
```python
feeder = Feeder()
chat_id = feeder.get_chatId(source='news_chatid')  # 'news_chatid' 소스의 채팅 ID를 반환합니다.
```

> `get_feed_ids(key)`
이메일 정보에 대한 키 값을 반환합니다.
- `key`: 키 값
``` python
feeder = Feeder()
usr_info = feeder.get_feed_ids(key='usr')  # 'usr' 키에 해당하는 이메일 정보를 반환합니다.
```
---
<br>
## Sender 클래스 퀵 가이드
`Sender` 클래스는 텔레그램 봇의 프로필 정보를 관리하고 토큰을 반환하는 클래스입니다.

### 클래스 생성 및 초기화
```python
bot_profiles = Bot_Profiles()
```
`Bot_Profiles` 클래스의 인스턴스를 생성합니다.

### 토큰 정보
`profiles` 속성은 텔레그램 봇의 토큰 정보를 딕셔너리로 저장합니다.
```python
{
    'token': 'telegram token',  # 텔레그램 봇의 토큰 정보
}
```

### 클래스 메서드
> `get_token() -> str`
텔레그램 봇의 토큰을 반환합니다.
```python
bot_profiles = Bot_Profiles()
bot_token = bot_profiles.get_token()  # 텔레그램 봇의 토큰을 반환합니다.
```
