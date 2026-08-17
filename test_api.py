import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OMDB_API_KEY")
url = f"http://www.omdbapi.com/?apikey={api_key}&t=Breaking Bad"

response = requests.get(url)
print(response.json())