import os


class Config(object):
    API_HASH = os.environ.get("e84dd69cd0504b8b45b2fd6a4e19068d")
    BOT_TOKEN = os.environ.get("7089320977:AAEOrgDFbECDKfgVCo8193HD9XSH7t3AMP0")
    TELEGRAM_API = os.environ["16073849"]
    OWNER = os.environ.get("5536032493")
    OWNER_USERNAME = os.environ.get("Shreeshiva323")
    PASSWORD = os.environ.get("Bshegde2481")
    DATABASE_URL = os.environ.get("mongodb+srv://viratfilter:virat123@cluster0.0ug4o4o.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1002116430363")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
