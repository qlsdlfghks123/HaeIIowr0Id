import requests
import json
import yaml


def get_access_token(config):
    url_base = "https://openapivts.koreainvestment.com:29443"
    headers = {"content-type": "application/json"}
    body = {
        "grant_type": "client_credentials",
        # grant_type = > 토큰 요청.
        "appkey": config['paper_app'],
        "appsecret": config['paper_sec']
        # appkey, appsecret : config[''] ==> yaml 파일에 있는 앱키와 시크릿 키 읽어오기
    }
    res = requests.post(f"{url_base}/oauth2/tokenP",
                        headers=headers,
                        data=json.dumps(body))
    return res.json().get('access_token')


def revoke_token(config, token):
    url_base = "https://openapivts.koreainvestment.com:29443"
    headers = {"content-type": "application/json"}
    body = {
        "appkey": config['paper_app'],
        "appsecret": config['paper_sec'],
        "token": token
    }
    res = requests.post(f"{url_base}/oauth2/revokeP",
                        headers=headers,
                        data=json.dumps(body)
                        )
    return res.json()
