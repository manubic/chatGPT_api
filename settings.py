from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()

class Settings:
    def __init__(self) -> None:
        self.APIKEY: str = os.environ.get('APIKEY')
        self.DBNAME: str = os.environ.get('DBNAME')
        self.DBUSER: str = os.environ.get('DBUSER')
        self.PASSWORD: str = os.environ.get('PASSWORD')
        self.HOST: str = os.environ.get('HOST') 
        self.PORT: str = os.environ.get('PORT')
        self.CLIENT: OpenAI = OpenAI(api_key = self.APIKEY)

settings = Settings()