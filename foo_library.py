import json

def get_thing(foo=None):
  if foo:
    # This might in reality make a database call, of course
    data = {"status":"okay", "foo": str(foo)}
    return data
  return None

def get_woo(bar=None):
  if bar:
    return {"one":"two", "three":"four"}
  return None
