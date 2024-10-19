from datetime import datetime
from pydantic import BaseModel

class Cryptocurrency(BaseModel):
    coingecko_id: str
    symbol: str
    name: str
    current_price: float
    market_cap: float
    total_volume: float
    last_updated: datetime
