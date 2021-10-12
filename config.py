import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBRsaVuXIVgFPbDaVbXw0lIbQOfTZ34QWWypjO0EZ3kbK58jVETgHAQUBXVsNXSxj2-spf1p4emRxlPDHB7Sd9n5xm-n_1KVKSIITzS2q91RJertFsIVaOkCegvkVSfVKrQr26X-THD8rU2hmSOecLTo6FcaE8jMYB_1HpL5KM5Fw0rLvcbI3YwEHheE1mEbbjz4DW8SwiPa4bip0UZbPVBXTt4ZPlDUmAgEGVT_ZuVfN_17gsb20uBLsZANmLKjQALyrTOySd9dHb-XY5vK29Wb_lDIhM63CXjyoU_s0eLEajfBSHcOPMatnnHXVK-DMliP8Rv-gpA5ZqBUYH3gmmedYvptwA")
BOT_TOKEN = getenv("BOT_TOKEN", "1909128749:AAGNB2Tblr31pVSQ4ryOWmdi7vGNoL4-vVg")
BOT_NAME = getenv("BOT_NAME", "QueenSzzaaRobot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/c5b2bd8566cc8f0c7e671.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/60a7ddea7b01b60424ca0.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/60a7ddea7b01b60424ca0.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/60a7ddea7b01b60424ca0.png")
API_ID = int(getenv("API_ID", "8589410"))
API_HASH = getenv("API_HASH", "a00436dc173e5b9a2c207fef097b7c04")
BOT_USERNAME = getenv("BOT_USERNAME", "QueenSzzaaRobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "QueenSzzaa")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "EagleSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "adeevaprojectt")
OWNER_NAME = getenv("OWNER_NAME", "QueenSzzaa") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", "ENABLE")
OWNER_ID = int(os.environ.get("OWNER_ID", "1964392902")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://userbot12:userbot12@cluster0.yl4i8.mongodb.net/adeeva?retryWrites=true&w=majority") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001541629727")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False")) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1980328702 1916880196").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/izzy-adeeva/VeezMusic")
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
