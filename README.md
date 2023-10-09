# 프로젝트 명: Bot_Alert - 알리미

## 프로젝트 소개
Bot_Alert는 실시간 정보 수집과 Telegram 알림을 결합한 AI 기반 콘텐츠 알림 봇입니다. <br>
asyncio 및 웹 크롤링 기술을 사용하여 다양한 정보 소스로부터 데이터를 수집하고 Telegram 메시지로 사용자에게 알림을 보내줍니다. <br>
Bot은 주요 정보 소스(뉴스, 메일, RSS 피드 등)로부터 데이터를 수집하고, 설정된 주기에 따라 업데이트합니다. <br>

## 주요 기능
1. **다양한 정보 소스 수집**: `뉴스 웹 사이트` `이메일` `RSS 피드`에서 데이터를 수집합니다.
2. **Telegram 알림**: Telegram 메신저를 통해 사용자에게 `텍스트 메시지``이미지` 정보를 실시간으로 알립니다.
3. **알림 주기 설정**: 사용자는 정보 업데이트 주기를 설정할 수 있으며, 필요에 따라 알림을 받을 빈도를 조절할 수 있습니다.
4. **중복 알림 방지**: 수집된 정보는 내부 데이터베이스에 저장되어 중복 알림을 방지합니다.

## 사용 가이드
### 1. Bot 토큰 설정: Telegram 봇을 생성하고 토큰을 Bot에 설정합니다.
```python
bot = Bot_Alert()
bot.setToken("YOUR_BOT_TOKEN")
```

### 2. 정보 소스 설정: `ContentsHandler` 클래스를 사용하여 정보 소스를 추가하고 컨텐츠를 수집합니다.
```python
context = Context(label="News Alert", content=["New news article: ..."], botChatId="YOUR_CHAT_ID", dtype="msg")
contents_handler = ContentsHandler(context)
```
### 3. Bot 시작: 설정한 알림 주기에 따라 정보를 수집하고 전송합니다.
```python
bot.start(waitTime=1800)
```

### 4. 정보 소스 설정
Bot_Alert는 다양한 정보 소스를 지원합니다. 
각 정보 소스에 대한 설정은 `Src_Alert` 클래스에서 구성됩니다.

  - **SrcMail**: 이메일에서 정보를 추출합니다.
  - **SrcNews**: 웹 페이지에서 뉴스 기사를 추출합니다.
  - **SrcRss**: RSS 피드에서 정보를 추출합니다.

### 5. 사용자 정의
Bot_Alert를 사용자 정의하려면 다음을 고려해보세요.
  - **새로운 정보 소스 추가**: `Src_Alert` 클래스에서 새로운 데이터 수집기를 만들어 등록하세요.
  - **알림 형식 변경**: `ContentsHandler` 클래스에서 컨텐츠 처리 및 전송 방법을 수정하여 알림 형식을 변경하세요.
  - **Bot 동작 수정**: `Bot_Alert` 클래스에서 봇의 동작 및 알림 주기를 조정하여 사용자 정의 봇을 만들 수 있습니다.
