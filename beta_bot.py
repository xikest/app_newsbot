import logging

from bots.bot_xiks.bot_echo import Echobot
from info.bot_info import BotInfo

# Enable logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# logger = logging.getLogger(__name__)
TOKEN =BotInfo.BetaBot.get_token()

Echobot(TOKEN).start()
#




