import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import timedelta
import datetime
import sqlite3
from dotenv import load_dotenv
import os
import base64
import requests
import json



load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(client_id)
print(client_secret)

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")
    url = "https://accounts.spotify.com/api/token"
    headers= {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url,headers = headers,data=data)
    json_result = json.loads(result.content)
    print(json_result)
    token = json_result["access_token"]
    return token

def get_data(TOKEN):
    # DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
    # USER_ID = "Sonali Kubde"
    # headers = {
    #     "Accept" : "application/json",
    #     "Content-Type" : "application/json",
    #     "Authorization" : "Bearer {token}".format(token = TOKEN)
    # }
    # today = datetime.datetime.now()
    # yesterday = today - timedelta(days = 1)
    # yesterday_unix_timestamp = int(yesterday.timestamp())*1000
    # r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time = yesterday_unix_timestamp),headers = headers)
    # data = r.json()
    # print(data)
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization" : "Bearer" +TOKEN}
    result = requests.get(url,headers = headers)
    res = json.loads(result.content)
    print(res)


token = get_token()
print(token)
get_data(token)







