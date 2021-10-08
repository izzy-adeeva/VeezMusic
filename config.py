import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Veez Music")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/c5b2bd8566cc8f0c7e671.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/60a7ddea7b01b60424ca0.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/60a7ddea7b01b60424ca0.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/60a7ddea7b01b60424ca0.png")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "QueenSzzaaRobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "QueenSzzaa")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "EagleSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "adeeva-projectt")
OWNER_NAME = getenv("OWNER_NAME", "QueenSzzaa") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", "ENABLE")
OWNER_ID = int(os.environ.get("OWNER_ID")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False")) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/levina-lab/VeezMusic")
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
