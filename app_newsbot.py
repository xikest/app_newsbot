from fastapi import FastAPI
import logging
from bot import NewsBot
import uvicorn

logging.basicConfig(level=logging.ERROR)
app = FastAPI()
bot = NewsBot()

@app.get("/run_newsbot")
async def run_newsbot():
    
    await bot.start()
    return {"status": "Bot started successfully"}
    
@app.get("/check_db")
async def check_db():
    await bot.check_db()
    return {"status": " finish"}
    
    


# if __name__ == "__main__":
#     uvicorn.run("app_newsbot:app", host="0.0.0.0", port=8008)
    