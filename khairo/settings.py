import os
from dotenv import load_dotenv
load_dotenv("../.env")

DEBUG = os.getenv("DEBUG")