#!/usr/bin/env python

import json
import foo_library
import inspect

data = {}
functions = inspect.getmembers(foo_library, inspect.isfunction)
for name, function in functions:
  method, endpoint = name.split('_')
  if endpoint not in data:
    data[endpoint] = []
  if method not in data[endpoint]:
    data[endpoint].append(method)

print json.dumps(data, indent=2)
