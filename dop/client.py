import os
import socket

from datacrunch import DataCrunchClient
from dotenv import load_dotenv


load_dotenv()


CLIENT_SECRET = os.environ["DATACRUNCH_CLIENT_SECRET"]
CLIENT_ID = os.environ["DATACRUNCH_CLIENT_ID"]
SSH_KEY_ID = os.environ.get("DATACRUNCH_SSH_KEY_ID")
IS_SPOT = bool(os.environ.get("DATACRUNCH_IS_SPOT", True))
HOSTNAME = os.environ.get("HOSTNAME", socket.gethostname())


client = DataCrunchClient(CLIENT_ID, CLIENT_SECRET)
