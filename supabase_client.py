import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

def get_supabase():
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

    if not SUPABASE_URL or not SUPABASE_ANON_KEY:
        raise ValueError("Supabase environment variables are missing")

    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

supabase = get_supabase()

