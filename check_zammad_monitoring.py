#!/usr/bin/python3
# Name      : check_zammad_monitoring.py
# Date      : 20221111
# Author    : Erik Exner - erik.exner@it-exner.de
# Summary   : This is a icinga check plugin that checks the builtin zammad monitoring url for health
# License   : Apache 2.0

import sys
import requests
import json
import argparse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser(description="check_zammad_monitoring")
parser.add_argument("-H", "--host", dest="host", help="The zammad monitoring url with http:// | https://, without '?token=XXX'", required=True)
parser.add_argument("-t", "--token", dest="token", help="The token to use, found in Webfrontend", required=True)
parser.add_argument("-k", "--insecure", dest="insecure", help="Dont verify the ssl-certificate", default=False, action=argparse.BooleanOptionalAction)
args = parser.parse_args()

if args.host:
    if args.insecure:
        x = requests.get(args.host + "?token=" + args.token, verify=False)
    else:
        x = requests.get(args.host + "?token=" + args.token, verify=True)
    if x.status_code == 200:
        data = json.loads(x.text)
        healthy = data['healthy']
        if healthy == True:
            print("All good!")
            sys.exit(0)
        else:
            message = "Unhealthy! "
            for i in data['issues']:
                message = message + "| " + i
            print(message)
            sys.exit(2)
    elif x.status_code == 401:
        print("Wrong Token: " + str(x.status_code))
        sys.exit(3) #Unknown
    else:
        print("Something gone wrong: " + str(x.status_code))
        sys.exit(3) #Unknown
else:
    print("Missing arguments")
    sys.exit(3) #Unknown
