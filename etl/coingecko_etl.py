import requests
from datetime import datetime, timedelta
from database import get_db
from config import  COINGECKO_API_URL
from repositories.crypto_repository import CryptoRepository
from models.cryptocurrency import Cryptocurrency

def fetch_crypto_data(crypto_id):
    response = requests.get(f"{COINGECKO_API_URL}/coins/{crypto_id}")
    print('------result----------')
    print(response.json())
    return response.json()

def fetch_historical_data(crypto_id, days=30):
    end_date = datetime.now()
    start_date = end_date.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=days)
    response = requests.get(param)

    requests.get(
        f"{COINGECKO_API_URL}/coins/{crypto_id}/market_chart/range",
        params={
            "vs_currency": "usd",
            "from": int(start_date.timestamp()),
            "to": int(end_date.timestamp())
        }
    )
    return response.json()

def transform_crypto_data(raw_data):
    return Cryptocurrency(
        coingecko_id=raw_data["id"],
        symbol=raw_data["symbol"].upper(),
        name=raw_data["name"],
        current_price=raw_data["market_data"]["current_price"]["usd"],
        market_cap=raw_data["market_data"]["market_cap"]["usd"],
        total_volume=raw_data["market_data"]["total_volume"]["usd"],
        last_updated=datetime.now()
    )

def transform_historical_data(raw_data, crypto_id):
    """Transform historical data to match our price_history table."""
    return [
        {
            "cryptocurrency_id": crypto_id,
            "price": price[1],
            "market_cap": market_cap[1],
            "total_volume": volume[1],
            "timestamp": datetime.fromtimestamp(price[0] / 1000).isoformat()  # Convert to ISO format string
        }
        for price, market_cap, volume in zip(
            raw_data["prices"],
            raw_data["market_caps"],
            raw_data["total_volumes"]
        )
    ]

def load_crypto_data(data):
    repo = CryptoRepository()
    result = repo.upsert_cryptocurrency(data)
    return result.data[0]['id']

def load_historical_data(data):
    """Load historical price data into the database."""
    db = get_db()
    db.table("price_history").insert(data).execute()

def run_etl(crypto_ids):
    for crypto_id in crypto_ids:
        # Extract
        crypto_data = fetch_crypto_data(crypto_id)
        historical_data = fetch_historical_data(crypto_id)

        # Transform
        transformed_crypto = transform_crypto_data(crypto_data)

        # Load cryptocurrency data and get its ID
        db_crypto_id = load_crypto_data(transformed_crypto)
        # Transform and load historical data
        transformed_history = transform_historical_data(historical_data, db_crypto_id)
        load_historical_data(transformed_history)

    print("ETL process completed successfully.")
