import json

def get_server(environment=None):
  if environment:
    # This might in reality make a database call, of course
    data = {"status":"okay", "environment": str(environment)}
    return data
  return None

def get_user(name=None):
  if name:
    data = {"status":"okay", "name": str(foo)}
    return data
  return None
