import urllib.request
from bs4 import BeautifulSoup
import re
from collections import defaultdict
url = 'http://shakespeare.mit.edu/hamlet/full.html'


def hamlet(url):
    with urllib.request.urlopen(url) as response:
        soup = BeautifulSoup(response.read(), 'html.parser')
    tags = soup.find_all('a', attrs={'name': re.compile('speech[0-9]+')})
    d = defaultdict(int)

    for tag in tags:
        d[tag.text] += 1

    tags2 = soup.find_all('a', attrs = {'name' : re.compile('^[0-9]+.*')})
    num_lines = len(tags2)
    num_speeches = len(tags)

    return num_lines, num_speeches, d
print(hamlet(url))