import requests
import json
import inspect
import sys
from requests import Request, Session
import pprint

schema = { "thing" : { "get" : ['foo'] } }

class Foo_Client(object):

  def __init__(self, hostname='localhost', port=5000):
    self.hostname = hostname
    self.port = port
    self.url = 'http://' + self.hostname + ':' + str(self.port)
    for name in schema:
      for method in schema[name]:
        function_name = method + '_' + name
        setattr(self, function_name, self.func)

  def func(self, **kwargs):
    for k, v in vars(self).items():
      if inspect.ismethod(v):
        function_name = k
        break

    method, path = function_name.split('_')
    method = method.upper()
    url = self.url + '/' + path
    data = kwargs

    header = {'content-type':'application/json'}

    s = Session()
    req = Request(method, url,
        data=json.dumps(kwargs),
        headers=header
    )
    prepped = req.prepare()

    r = s.send(prepped)
    return r.text
