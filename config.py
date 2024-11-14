import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21374834"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1086db70452e2d8f69e748966c714ee2")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://04eqga159c:yWiJuQShlRMgogY9@cluster0.ycbco.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
