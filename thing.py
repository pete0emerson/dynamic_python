#!/usr/bin/env python

import foo_client

# A simple example of leveraging the Python client
# which leverages the API
# which leverages the library

c = foo_client.Foo_Client()

print c.get_thing(foo='banana')
