# APA-Kit
Small tool under development based on vulnerability scaning
## Getting Started
just clone it! ready to use!
## How-To-Use
Simple!
```
python main.py -s example.com [--switches]
```
[--switches]
* -s SERVER, --server=SERVER : specify target URLs with http(s) [http(s)://example.com]
* -p PORT, --port=PORT : specify target file with URLs
* -r, --resolve : hostname to ip
* -o OPENPORT, --openport=OPENPORT : Open Port Scanning
* -e, --header : extract header info

## Port Scanner
### Start
Example:
```
python main.py -s google.com -o 25,80,443
```
### Stop
```
Url has been set! [google.com]
Port 80 is open
Port 443 is open
Port 25 is close
```
## Resolver
### Start
```
python main.py -s google.com -r
```
### Stop
```
Url has been set! [google.com]
ip >>> [172.217.21.238]
Done!
```
## HTTP Header Grabbing
### Start
```
python main.py -s google.com -e
```
### Stop
```
Header status code >>> <Response [200]>
Date : Mon, 12 Nov 2018 19:17:29 GMT
Expires : -1
Cache-Control : private, max-age=0
Content-Type : text/html
charset=ISO-8859-1
P3P : CP="This is not a P3P policy! See g.co/p3phelp for more info."
Content-Encoding : gzip
Server : gws
Content-Length : 4906
X-XSS-Protection : 1
mode=block
X-Frame-Options : SAMEORIGIN
Set-Cookie : 1P_JAR=2018-11-12-19
expires=Wed, 12-Dec-2018 19:17:29 GMT
path=/
domain=.google.com, NID=146=1qtlbRUF30AwDVN3mHiWM004oWpAOpA7SKSSF3OjsT0klVSIoNjlXofvK9ysYAaTGvGnjV1hwF9wz3hCsqa1Nk-PvMECMnKJmr97rudUsOUBMp1wBkLhDZx1Gn4pLymRCf0EfACVMQNYGGf2azTZ0wfYf2TkGNo-iR04gnHNEUM
expires=Tue, 14-May-2019 19:17:29 GMT
path=/
domain=.google.com
HttpOnly
```
