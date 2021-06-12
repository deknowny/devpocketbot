import os

import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())


GROUP_BOT_TOKEN = os.getenv("GROUP_BOT_TOKEN")


CLIENT_ID = int(os.getenv("CLIENT_ID"))
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

SERVER_IP = os.getenv("SERVER_IP")
SERVER_PORT = int(os.getenv("SERVER_PORT"))