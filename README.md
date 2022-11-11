# check_zammad_monitoring
Simple script to check the output of the builtin zammad monitoring url.

```
usage: check_zammad_monitoring.py [-h] -H HOST -t TOKEN [-k | --insecure | --no-insecure]

check_zammad_monitoring

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  The zammad monitoring url with http:// | https://, without '?token=XXX'
  -t TOKEN, --token TOKEN
                        The token to use, found in Webfrontend
  -k, --insecure, --no-insecure
                        Dont verify the ssl-certificate (default: False)
```
