import requests
import time
import os
HOST = os.getenv('HOST', 'localhost')
METHOD = os.getenv('METHOD', 'get')

for idx in range(10000):
    try:
        if METHOD == 'get':
            res = requests.get("http://%s/healthcheck"%(HOST)).json()
        else:
            res = requests.post("http://%s/healthcheck"%(HOST)).json()
        print(res)
        time.sleep(0.5)
    except:
        time.sleep(1)
