import json
from urllib.request import urlopen
from time import localtime,asctime
import datetime

def load_product(url):
    data = urlopen(url)
    data_json =json.loads(data.read())
    return data_json
