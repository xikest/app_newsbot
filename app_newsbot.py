from fastapi import FastAPI
import logging
from bot import NewsBot
import uvicorn

logging.basicConfig(level=logging.ERROR)
app = FastAPI()

@app.get("/run_newsbot")
async def run_newsbot():
    bot = NewsBot()
    await bot.start()
    return {"status": "Bot started successfully"}
    

if __name__ == "__main__":
    uvicorn.run("app_newsbot:app", host="0.0.0.0", port=8008)
    