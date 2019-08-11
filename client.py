import requests
import time
import os
HOST = os.getenv('HOST', 'localhost')

for idx in range(10000):
    try:
        res = requests.get("http://%s/healthcheck"%(HOST)).json()
        print(res)
        time.sleep(0.5)
    except:
        time.sleep(1)
