import os
from dotenv import load_dotenv
load_dotenv()

TERAKOYA_GMAIL_ADDRESS = os.getenv("TERAKOYA_GMAIL_ADDRESS")
TERAKOYA_GMAIL_PASSWORD = os.getenv("TERAKOYA_GMAIL_PASSWORD")
TERAKOYA_GROUP_MAIL_ADDRESS = os.getenv("TERAKOYA_GROUP_MAIL_ADDRESS")