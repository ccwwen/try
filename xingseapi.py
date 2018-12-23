# coding=utf-8
import base64
import urllib, urllib2, sys
import ssl


host = 'https://plantapi.xingseapp.com'
path = '/item/identification'
method = 'POST'
appcode = '38ef43ff3c704a7c8bc5f934185b3a3d'
querys = ''
bodys = {}
url = host + path

with open(u"./pics/杜鹃.jpeg", "rb") as image_file:

    bodys['image_data'] = base64.b64encode(image_file.read()).decode('ascii')
    post_data = urllib.urlencode(bodys)
    request = urllib2.Request(url, post_data)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    ##根据API的要求，定义相对应的Content-Type
    request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib2.urlopen(request, context=ctx)
    content = response.read()
    if (content):
        print(content)
