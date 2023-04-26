# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "28365363"))
API_HASH = os.environ.get("API_HASH", "474776dc7ed27e73a8c9d64915421b6f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5934477504:AAHRAbdqvsr3Zn0gRDnPF-3PW7OM2nhyEuM")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1952868714")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Yaseen23")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Yaseen23:<password>@yaseen1.vpqaond.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1952868714")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Updates Channel User name Without @") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
