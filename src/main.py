import os

import logging
from bowot import Bowot
from dotenv import load_dotenv
load_dotenv()


BOT_TOKEN = os.getenv('BOWOT_TOKEN')
BOT_ID = os.getenv('BOWOT_ID')
BOT_PERMISSIONS = os.getenv('BOWOT_PERMISSIONS')


logging.basicConfig(level=logging.INFO)


def main():
    bot = Bowot(BOT_ID, BOT_PERMISSIONS)
    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
