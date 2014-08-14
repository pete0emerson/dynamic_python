#!/usr/bin/env python

import foo_library
import inspect
import sys
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
  method = request.method.lower()
  function_name = method + '_' + path

  # Make sure we've got a valid request (i.e. the function exists)
  try:
    f = getattr(foo_library, function_name)
  except:
    return '{"status":"error":"message":"Invalid request"}\n', 404

  # Make sure the user has passed in JSON
  try:
    data = request.get_json(force=True)
  except:
    return '{"status":"error":"message":"No JSON passed"}\n', 404

  # Make sure the user has passed in the required parameters for the function
  for arg in inspect.getargspec(f).args:
    if arg not in data:
      return '{"status":"error":"message":"' + arg + ' not found in JSON' + '"}\n', 400

  results = f(**data)
  return json.dumps(results) + '\n'

if __name__ == "__main__":
  app.run(debug = True, use_reloader=True, port = 5000)
