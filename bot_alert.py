import asyncio
import platform

from bots.bot_alert.bot_news_alert import NewsAlert
from bots.src_generator.src_alert import SrcAlert
from info.bot_profiles import BotProfiles



TOKEN = BotProfiles.get_botTwitters().TOKEN
# TOKEN = BotProfiles.get_botAlert().TOKEN
srcAlert = SrcAlert()
srcAlert.set_chatId_mail( BotProfiles.get_botTwitters().channels.get('chat_id'))
srcAlert.set_chatId_news( BotProfiles.get_botTwitters().channels.get('chat_id'))
srcAlert.set_chatId_rss( BotProfiles.get_botTwitters().channels.get('chat_id'))


if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(NewsAlert(TOKEN).update(srcAlert.generator))

