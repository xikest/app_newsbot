import asyncio
import platform

from bots.bot_alert.bot_news_alert import NewsAlert
from bots.src_generator.src_alert import SrcAlert
from info.bot_profiles import BotProfiles



TOKEN = BotProfiles.get_botAlert().TOKEN
srcAlert = SrcAlert()

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(NewsAlert(TOKEN).update(srcAlert.generator))

