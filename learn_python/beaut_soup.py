import urllib
from BeautifulSoup import * # this is unusual

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

#  Retrieve a list of the anchor tags
#  each tag is like a dictionary of HTML attributes

tags = soup('a')

for tag in tags:
    print tag.get('href', None)
