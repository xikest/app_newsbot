

import asyncio

from bots.bot_alert.bot_news_alert import NewsAlert
# from bots.bot_xiks.bot_echo import Echobot
from bots.bot_alert.src_generator.src_news import SrcNews


# #beta testing
token = '5640649486:AAHVTR7NQF1n5InXaKtTp7CcUfDUOgQ0D00'
chat_id='-1001601197449'

newsBot = NewsAlert(token)

SrcNews.setChatId(chat_id)
SrcNews.NBER.setChatId(chat_id)




import platform
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(NewsAlert(token).start(SrcNews.gen_news))
