from fastapi import FastAPI
from config import PORT, HOST
from router.router import router as crypto_router
from etl.coingecko_etl import run_etl
from config import CRYPTOCURRENCIES_TO_FETCH

app = FastAPI(title="Cryptocurrency API", host=HOST, port=PORT)

# Include the router
app.include_router(crypto_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Cryptocurrency Analytics Projectdssss!"}
