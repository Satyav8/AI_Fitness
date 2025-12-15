from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def get_supabase() -> Client:
    """Returns a singleton Supabase client"""
    return create_client(SUPABASE_URL, SUPABASE_KEY)

# Export the supabase instance for easy importing
supabase = get_supabase()
