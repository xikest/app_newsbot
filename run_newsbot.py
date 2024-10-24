import asyncio
import logging
from fastapi import FastAPI
from pydantic import BaseModel
from bot import Bot

# 로깅 설정
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class ScraperRequest(BaseModel):
    # 필요 시 요청 데이터 모델 정의
    pass

@app.post("/run_newsbot")
async def run_bot(scraper_request: ScraperRequest):
    bot = Bot()
    await bot.start()
    return {"status": "bot started"}