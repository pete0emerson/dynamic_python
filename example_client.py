#!/usr/bin/env python

from foo_client import Foo_Client

# A simple example of leveraging the Python client
# which leverages the API
# which leverages the library

if __name__ == "__main__":
  client = Foo_Client()
  print client.get_server(environment='stage')
  print client.get_user(name='Pete')

