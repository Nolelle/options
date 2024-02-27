from polygon import RESTClient
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("polygon_api_key")

client = RESTClient(api_key=api_key, trace=True)
