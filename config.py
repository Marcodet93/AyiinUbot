from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")


flood = {}
OLD_MSG = {}
MSG_PERMIT = (
    """
ʜᴀʟᴏ ᴛᴏᴅ.

sᴀʙᴀʀ ᴛᴏᴅ ɪɴɪ ᴘᴇsᴀɴ ᴏᴛᴏᴍᴀᴛɪs

ᴛᴜɴɢɢᴜ Lᴇxᴀ ᴛᴇʀɪᴍᴀ ᴘᴍ ʟᴜ.

ᴊᴀɴɢᴀɴ sᴘᴀᴍ ᴀᴛᴀᴜ ᴋᴀʟɪᴀɴ ᴀᴋᴀɴ ᴅ ʙʟᴏᴋ ᴏᴛᴏᴍᴀᴛɪs ᴏʟᴇʜ ʙᴏᴛ.

Lᴇxᴀ ꭙ 𝛌ᴍᴀɴᴅ𐐩s♔
"""
)


class Var:
    API_HASH = getenv("API_HASH")
    API_ID = int(getenv("API_ID", ""))
    ALIVE_PIC = getenv("ALIVE_PIC", ""https://telegra.ph/file/08a826d4a7460dc2fd74a.jpg)
    ALIVE_TEXT = getenv("ALIVE_TEXT", "Yo tod:v")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
    if not BLACKLIST_CHAT:
        BLACKLIST_CHAT = [-1001473548283, -1001675396283]
    LOG_CHAT = int(getenv("LOG_CHAT") or 0)
    HNDLR = getenv("HNDLR", [".", "!", "*", "^", "-", "?"])
    DB_URL = getenv("DATABASE_URL", "")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
    MONGO_URI = getenv("MONGO_URI", None)
    NO_LOAD = [int(x) for x in getenv("NO_LOAD", "").split()]
    PMPERMIT = bool(getenv("PMPERMIT", True))
    PERMIT_MSG = str(getenv("PERMIT_MSG", MSG_PERMIT))
    PERMIT_LIMIT = int(getenv("PERMIT_LIMIT", 5))
    REM_BG_API_KEY = getenv("REM_BG_API_KEY", "WEnHwQnst3E2HzjGgwmy4UpB")
    STRING_1 = getenv("STRING_1", "")
    STRING_2 = getenv("STRING_2", "")
    STRING_3 = getenv("STRING_3", "")
    STRING_4 = getenv("STRING_4", "")
    STRING_5 = getenv("STRING_5", "")
    TEMP_DOWNLOAD_DIRECTORY = getenv("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
    TZ = getenv("TZ", "Asia/Jakarta")
