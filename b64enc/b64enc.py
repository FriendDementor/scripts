#!/bin/python3
# https://en.wikipedia.org/wiki/Base64

import argparse
import base64


parser = argparse.ArgumentParser(description='encode string in base64')
parser.add_argument('code', metavar='CODE', type=str, help='code')

args = parser.parse_args()

message = args.code
message_bytes = message.encode('utf-8')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('utf-8')

print(base64_message)
