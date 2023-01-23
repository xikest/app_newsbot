import asyncio
import platform

from bots import BotAlert
from bots.src_generator import SrcAlert
from info.bot_profiles import BotProfiles

# ==========================================================================================
#  테스트 프로파일
# ==========================================================================================

TOKEN = BotProfiles.get_botBeta().TOKEN
srcAlert = SrcAlert()
srcAlert.set_chatId_insight( BotProfiles.get_botBeta().channels.get('beta_chat_id'))
srcAlert.set_chatId_wsj( BotProfiles.get_botBeta().channels.get('beta_chat_id'))
srcAlert.set_chatId_news( BotProfiles.get_botBeta().channels.get('beta_chat_id'))
srcAlert.set_chatId_tweetsMacro( BotProfiles.get_botBeta().channels.get('beta_chat_id'))
srcAlert.set_chatId_concensus( BotProfiles.get_botBeta().channels.get('beta_chat_id'))
srcAlert.set_chatId_energy( BotProfiles.get_botBeta().channels.get('beta_chat_id'))
srcAlert.set_chatId_cn( BotProfiles.get_botBeta().channels.get('beta_chat_id'))
srcAlert.set_chatId_agri( BotProfiles.get_botBeta().channels.get('beta_chat_id'))
srcAlert.set_chatId_stats( BotProfiles.get_botBeta().channels.get('beta_chat_id'))
srcAlert.set_chatId_bok( BotProfiles.get_botBeta().channels.get('beta_chat_id'))




# ==========================================================================================
#  프로파일
# ==========================================================================================

TOKEN = BotProfiles.get_botAlert().TOKEN
srcAlert = SrcAlert()


# ==========================================================================================
#  실행
# ==========================================================================================
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
asyncio.run(BotAlert(TOKEN).start(srcAlert.generator))

