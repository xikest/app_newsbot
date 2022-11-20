import asyncio
import platform

from bots.bot_alert.bot_news_alert import NewsAlert
from bots.src_generator.src_news import SrcNews
from info.bot_info import BotInfo

# #beta testing
TOKEN =BotInfo.AlertBot.get_token()
SrcNews.setChatId(BotInfo.AlertBot.get_chanel('teat_chat_id'))
SrcNews.Mailbox.setChatId(BotInfo.AlertBot.get_chanel('teat_w_chat_id'))
SrcNews.NBER.setChatId(BotInfo.AlertBot.get_chanel('nber_chat_id'))
SrcNews.Tweets.setChatId(BotInfo.AlertBot.get_chanel('twt_chat_id'))

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(NewsAlert(TOKEN).start(SrcNews.gen_news))

