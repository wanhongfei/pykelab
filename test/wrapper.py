# -*- coding: utf-8 -*-

token = "partner=tt&timestamp=1502088838.24&nonce=123&signature=cd7a6ef3c6518ea210035f98683d988940202885&access_token=c242cd5640fb0f340ed7c7fac159fdc6"
feed_uri = "http://10.6.131.78:10073/data/stream/v3/?"
video_uri = "http://open.snssdk.com/data/video/url/v1/?"

import json
import urllib2

def get(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html = response.read()
    data = json.loads(html)
    return data


total = 0
error = 0

while (total < 1000):
    data = get(feed_uri + token)
    print "===>total,error:", total, error
    for card in data['data']:
        if card.get('video_id'):
            total = total + 1
            video_id = card.get('video_id')
            video_data = get(video_uri + token + "&video_id=" + video_id)
            if video_data['data'].get('status') != 10:
                error = error + 1
        if total == 1000:
            break

print "error/total*100%:", error * 1.0 / total
