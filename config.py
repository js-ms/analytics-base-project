import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_API_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
COINGECKO_API_URL = os.getenv("COINGECKO_API_URL")
CRYPTOCURRENCIES_TO_FETCH = ['bitcoin', 'ethereum']

# Server configuration
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
