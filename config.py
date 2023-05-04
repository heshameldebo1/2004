from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "12435961"))
API_HASH = getenv("API_HASH", "f554d351fe95ad41c31540514e7f5623")
BOT_TOKEN = getenv("BOT_TOKEN", "6152028137:AAHnF5biz0HTB85jzmzEEK6tXFUFyKUrFHk")
SESSION_NAME = getenv("SESSION_NAME", "1BJWap1sBu6QNOhIyT60CunVgwPfAC3a-9ZPQr9KX3sL1uRhNKykvBepaCIj8UrV_iP9iN7FkKALtNR1LP4pDV38YPYTKDmFbw-0J50-zLMuvYKlWbTT10OLuHk2cmLrQctPzUOAvlg-iITT-vDpuK9a9MP-sxTYkdCAnlrg8-_uqrcw57clwOTk522e66irR6LBhPNal_0nio-t3np5BguNbzv_cpSQlpn0ks54X9UWf1EFTr9BBCOfz2UDSj-veBzMiFri_3GAidSRZRLOe_5cZV-RVI0AyszXGAUKYk7gNdBT4ddO4o7XE092k_FgViYkc92QoXzohgfTW6LcuUU4ljdpa36M=

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Eldebo3")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "eldebomusic_bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "eldeboY")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "eldeboY")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
