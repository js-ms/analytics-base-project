from models.cryptocurrency import Cryptocurrency
from database import get_db

class CryptoRepository:
    def __init__(self):
        self.db = get_db()

    def get_all_cryptocurrencies(self):
        response = self.db.table('cryptocurrencies').select('*').execute()
        return [Cryptocurrency(**crypto) for crypto in response.data]

    def get_cryptocurrency_by_symbol(self, symbol: str):
        response = self.db.table('cryptocurrencies').select('*').eq('symbol', symbol).execute()
        return Cryptocurrency(**response.data[0]) if response.data else None

    def upsert_cryptocurrency(self, crypto: Cryptocurrency):
        crypto_data = {
            "coingecko_id": crypto.coingecko_id,
            "symbol": crypto.symbol,
            "name": crypto.name,
            "current_price": crypto.current_price,
            "market_cap": crypto.market_cap,
            "total_volume": crypto.total_volume,
            "last_updated": crypto.last_updated.isoformat()
        }
        return self.db.table("cryptocurrencies").upsert(crypto_data, on_conflict=["coingecko_id"]).execute()
