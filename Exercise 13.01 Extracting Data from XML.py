import urllib.request as ur
import xml.etree.ElementTree as et
#url = input('Enter location: ')
# 'http://python-data.dr-chuck.net/comments_42.xml'
url="http://py4e-data.dr-chuck.net/comments_1360657.xml"
total_number = 0
sum = 0
print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')
tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_number += 1
print('Count:', total_number)
print('Sum:', sum)
