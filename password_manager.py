import json
import hashlib
import os

DATA_FILE = "passwords.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def setup_master_pasword():
    master = 
    