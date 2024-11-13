from fastapi import FastAPI
import logging
from bot import NewsBot
# import uvicorn

logging.basicConfig(level=logging.ERROR)

app = FastAPI()

async def main():
    bot = NewsBot()
    await bot.start()

@app.get("/run_newsbot")
async def run_calendar():
    await main()
    return {"status": "Bot started successfully"}
    

# if __name__ == "__main__":
#     uvicorn.run("app_newsbot:app", host="0.0.0.0", port=8008)
    