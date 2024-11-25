import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os

load_dotenv()

cred = credentials.Certificate(os.getenv("PATH_TO_SERVICE_ACCOUNT_KEY"))

firebase_admin.initialize_app(cred)

db = firestore.client()