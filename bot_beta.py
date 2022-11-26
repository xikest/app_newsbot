import logging

from bots.bot_xiks.bot_echo import Echobot
from info.bot_profiles import BotProfiles

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = BotProfiles.get_botBeta().TOKEN
Echobot(TOKEN).start()
