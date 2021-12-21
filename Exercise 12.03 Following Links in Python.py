# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def webscrap(url, count, position, tc):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    sum=0
    for tag in tags:
        sum=sum+1        
        if sum == position:
            url=tag.get('href', None)
            print(url)
            if tc == count:
                print('Contents:',tag.contents[0])
            else:
                url=tag.get('href', None)
                tc=tc+1
                webscrap(url, count, position, tc)
            break
#url = input('Enter URL:')
#count=input('Enter count:')
#position=input('Enter position:')
url =  "http://py4e-data.dr-chuck.net/known_by_Rubyn.html"
count=7
position=18
tc = 1
webscrap(url, int(count), int(position), int(tc))
