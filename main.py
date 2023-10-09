import asyncio
import platform
import logging

from bot import Bot

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
async def main():
    bot = Bot()
    await bot.start()

if __name__ == '__main__':
    asyncio.run(main())

# # ==========================================================================================
# #  프로파일
# # ==========================================================================================
#
# # TOKEN = BotProfiles.get_bot_token()
# # srcAlert = SrcAlert()
#
# # ==========================================================================================
# #  실행
# # ==========================================================================================
# if platform.system()=='Windows':
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#
# asyncio.run(BotAlert().start())
#
# if __name__ == '__main__':
#     bot = BotAlert()
#     asyncio.run(bot.start())