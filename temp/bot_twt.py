import asyncio
import platform

from bots.bot_alert.bot_news_alert import NewsAlert
from bots.src_generator.srcAlert.src_tweets import SrcTweets
from info.bot_profiles import BotProfiles
from info.bot_ids import InfoTwitter
from info.feeds import FeedFlowwings


TOKEN = BotProfiles.get_botTwitters().TOKEN

srcTwitter = SrcTweets(BEARERTOKEN = InfoTwitter.get_twitter_BEARERTOKEN(), 
                        screenNames = FeedFlowwings.get_screenNames,
                        ChatId = BotProfiles.get_botTwitters().channels.get('twt_chat_id'))
                        # ChatId = BotProfiles.get_botTwitters().channels.get('chat_id'))

if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    

asyncio.run(NewsAlert(TOKEN).start(srcTwitter.generator, waitTime= 1*60))


