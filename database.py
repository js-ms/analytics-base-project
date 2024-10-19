from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

class Database:
    _instance = None

    @classmethod
    def get_instance(cls) -> Client:
        if cls._instance is None:
            cls._instance = create_client(SUPABASE_URL, SUPABASE_KEY)
        return cls._instance

# This function is used for dependency injection in FastAPI
def get_db():
    return Database.get_instance()
