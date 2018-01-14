import requests
import urllib.parse
import time
import hmac
import base64
import hashlib
from cerberus.auxiliary.yaml_validator import YamlValidator as yv

class BitmexWrapper:
    def __init__(self):
        self.root = "https://www.bitmex.com"

    def query(self, verb, path, params={}, data=""):
        expiry_time = str(int(time.time() + 60))
        destination = "/api/v1/" + path + urllib.parse.urlencode(params, doseq=True)
        sig = self.__generate_signature(verb, destination, expiry_time, data)
        url = self.root + "/api/v1/" + path
        headers = { 'api-expires': expiry_time, 'api-key': yv.find("bitmex_key"), 'api-signature': sig }
        return requests.get(url, headers=headers)

    def __generate_signature(self, verb, path, expiry_time, data=""):
        message = bytes(verb + path + expiry_time + data, 'utf-8')
        secret = bytes(yv.find("bitmex_secret"), 'utf-8')
        return hmac.new(secret, message, digestmod=hashlib.sha256).hexdigest()

