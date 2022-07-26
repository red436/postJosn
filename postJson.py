#!/usr/bin/python

import os
import sys
import requests
import json

jsonReq = json.loads(open(sys.argv[2], "r").read())

res = requests.post(sys.argv[1], json=jsonReq)

print(res.text)
