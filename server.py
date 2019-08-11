# coding: utf-8
import os
import falcon
import json
import urllib
import datetime
import random
import time

class NginxFailoverTestResource(object):
    status = falcon.HTTP_200
    delay = 0.1
    cnt = 1
    intermit_options = 0

    def on_get(self, req, resp, func=""):
        self.on_get_post(req, resp, func)

    def on_post(self, req, resp, func=""):
        self.on_get_post(req, resp, func)

    def on_get_post(self, req, resp, func=""):
        start_time = time.time()

        params = req.params

        status_list = {
            'res_200':falcon.HTTP_200,
            'res_400':falcon.HTTP_400,
            'res_404':falcon.HTTP_404,
            'res_408':falcon.HTTP_408,
            'res_500':falcon.HTTP_500,
            'res_502':falcon.HTTP_502,
            'res_503':falcon.HTTP_503,
            'res_504':falcon.HTTP_504
        }

        node_id = int(os.getenv('node_id','0'))
        # status = falcon.HTTP_200

        if 'intermit' in params:
            try:
                self.intermit_options = int(params['intermit'])
            except:
                self.intermit_options = 0

        if 'status' in params:
            if params['status'] in status_list:
                self.status = status_list[params['status']]

        if 'delay' in params:
            try:
                self.delay = float(params['delay'])
            except:
                self.delay = 0.1

        if not params:
            time.sleep(self.delay)

        # print(int(datetime.datetime.now().minute/10)%(node_id))
        # except_status = random.choice(list(except_response.values()))
        # if random.random() > 0.9:
        #     status = except_status

        end_time = time.time()

        status = self.status

        if self.intermit_options:
            self.cnt += 1
            if self.cnt % 20 < 5:
                # status = status_list['res_404']
                status = status_list['res_500']

        result = {
            'node_id' : 'node_%02d'%(node_id),
            'datetime' : str(datetime.datetime.now()),
            'delay' : end_time - start_time,
            'status' : status
        }

        print(json.dumps(result))

        resp.status = status
        resp.body = json.dumps(result)

        # if self.status is not falcon.HTTP_200:
        #     raise Exception('except test')

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
nginxFailoverTestResource = NginxFailoverTestResource()

# handler = NginxFailoverTestResource().on_get_post
# app.add_sink(NginxFailoverTestResource().on_get_post, prefix='/')
app.add_route('/healthcheck', nginxFailoverTestResource)
