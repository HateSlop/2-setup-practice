import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("API_KEY")
print("Your API Key is:", key)