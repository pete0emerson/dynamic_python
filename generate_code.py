#!/usr/bin/env python

import json
import inspect
import foo_library

def generator(function_name, method, endpoint):

  function_code = """
  def %s(self, **kwargs):
    method = '%s'
    endpoint = '%s'
    url = self.url + '/' + endpoint
    header = {'content-type':'application/json'}
    s = Session()
    req = Request(method, url,
        data=json.dumps(kwargs),
        headers=header
    )
    prepped = req.prepare()
    r = s.send(prepped)
    return r.text.rstrip()
"""
  print function_code % (function_name, method.upper(), endpoint)

class_code = """
from requests import Request, Session
import json

class Foo_Client:

  def __init__(self, config='./foo_client.json', hostname='localhost', port=5000):
    self.hostname = hostname
    self.port = port
    self.url = 'http://' + self.hostname + ':' + str(self.port)
"""

print class_code,
functions = inspect.getmembers(foo_library, inspect.isfunction)
for function_name, function in functions:
  method, endpoint = function_name.split('_')
  generator(function_name, method, endpoint)

# url = self.url + '/' + endpoint
# header = {'content-type':'application/json'}
# s = Session()
# req = Request(method, url,
#     data=json.dumps(kwargs),
#     headers=header
# )
# prepped = req.prepare()
# r = s.send(prepped)
# return r.text.rstrip()
