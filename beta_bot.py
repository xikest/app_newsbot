import logging
from bots.bot_alert.bot_news_alert import NewsAlert
from bots.bot_master import BotMaster
from bots.bot_alert.src_generator.src_news import SrcNews
from bots.bot_xiks.bot_echo import Echobot
import time

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# #beta testing
token = '5640649486:AAHVTR7NQF1n5InXaKtTp7CcUfDUOgQ0D00'
beta_chat_id= '-1001601197449'


Echobot(token).start()
# asyncio.run(a)
# asyncio.run()
print('fin')



