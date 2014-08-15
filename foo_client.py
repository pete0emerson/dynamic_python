#!/usr/bin/env python

from requests import Request, Session
import json

class Foo_Client:

  def __init__(self, hostname='localhost', port=5000):
    self.hostname = hostname
    self.port = port
    self.url = 'http://' + self.hostname + ':' + str(self.port)
    # This really should come from a file. Perhaps an auto-generated one.
    self.data = { 'server' : ['get'], 'user' : ['get']}

    for endpoint in self.data:
      for method in self.data[endpoint]:
        function_name = method + '_' + endpoint
        method = method.upper()
        setattr(self, function_name, self.wrap(method, endpoint))

  def wrap(self, method, endpoint):
    def  catch_all(**kwargs):
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
    return catch_all
