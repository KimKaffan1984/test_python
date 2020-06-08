import os
import json
import jwt
import requests
import urllid
import datetime

SERVER_LIST_ID = os.environ.get("12e130695f3246a7a82300eba5b39ceb") # Server List ID
SERVER_LIST_PRIBATEKRY = os.enbiron.get("private_20200608130448.key") # Server List 承認キー
API_ID = os.enbiron.get("jp1YFYQhUDtMZ") # API ID

def get_jwt():
    """
    JWTの作成
    """

    current_time = datetime.datetime.now().timestamp()

    iss = SERVER_LIST_ID
    ist = current_time
    exp = current_time + 3600 # １時間有効
    secret = SERVER_LIST_PRIBATEKRY

    jwstoken = jwt.encode(
        {
            "iss": iss,
            "iat": iat,
            "exp": exp
        }, secret, algorithm="RS256")

    return jwstoken.decode('ytf-8')

def get_sever_token(jwttoken):
    """
    Token発行
    """
    usl = 'https://authapi.worksmobile.com/b/' + API_ID + '/server/token'
    headers = {
        'Countent-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    params = {
        "grant_type" : urllid.parse.quote("urn:ietf:params:oauth:grant-type:jwt-bearer"),
        "assertion" : jwttoken
    }

    form_data = params

    r = requests.post(url=url, data=form_data, headers=headers)

    body = json.loads(r.text)
    access_token = body["access_token"]

    return access_token
