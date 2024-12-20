from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = " None "
# -------------------------------------------------------------
API_HASH = " None "
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "5923034665"))
SUPPORT_GRP = "FRIEND_KI_MASTI_CLUB"
UPDATE_CHNL = "NAINCY_UPDATES"
OWNER_USERNAME = "vishnusoni14"
