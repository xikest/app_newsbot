import asyncio
import platform
import time

from bots.bot_alert.bot_news_alert import NewsAlert
from bots.src_generator.src_tweets import SrcTweets
from info.bot_profiles import BotProfiles
from info.bot_ids import InfoTwitter


TOKEN = BotProfiles.get_botTwitters().TOKEN

srcTwitter = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                        screenNames = InfoTwitter.get_screenNames(),
                        ChatId = BotProfiles.get_botTwitters().channels.get('twt_chat_id'))

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
while True:
    asyncio.run(NewsAlert(TOKEN).update(srcTwitter.generator))
    print('cycle finish')
    #

