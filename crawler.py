import re
import sys
import urllib
import urlparse
import random
from bs4 import BeautifulSoup

#http://wolfprojects.altervista.org/articles/change-urllib-user-agent/
class MyOpener(urllib.FancyURLopener):
   version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'

#This function will parse a url to give you the domain. Test it!
def domain(url):
    #urlparse breaks down the url passed it, and you split the hostname up
    #Ex: hostname="www.google.com" becomes ['www', 'google', 'com']
    hostname = urlparse.urlparse(url).hostname.split(".")
    hostname = ".".join(len(hostname[-2]) < 4 and hostname[-3:] or hostname[-2:])
    return hostname

def normalize(url):
    pass

def parse_links(url):
    url_list = []
    myopener = MyOpener()
    try:
        #open, read, and parse the text using beautiful soup
        page = myopener.open(url)
        text = page.read()
        page.close()
        soup = BeautifulSoup(text)

        title = soup.find(id='firstHeading').span.text.encode('ascii')
        content = soup.find(id='mw-content-text')

        #find all hyperlinks using beautiful soup
        for tag in content.findAll('a', href=True):
            path = tag['href'].encode('ascii')
            if path[:6] == '/wiki/' and path[:10] != '/wiki/File':
                link = 'http://en.wikipedia.org' + path
                url_list.append(link)
        return title, url_list
    except:
        return []

title, urls = parse_links('http://en.wikipedia.org/wiki/FIS_Alpine_World_Ski_Championships_1978')
import pdb; pdb.set_trace()
#the url we want to begin with
url_start = "http://en.wikipedia.org/wiki/Special:Random"
current_url = url_start

#parameter to set the number of transitions you make/different pages you visit
num_of_visits = 100

#dictionary of pages visited so far
visit_history = {}

for i in range(num_of_visits):
    print 'Visiting... ', current_url

    #incrementing the counts
    visit_history[current_url] += 1

    #parsing all the links on the page
    url_list = parse_links(current_url, url_start)

    #returning a random link to go to
    current_url = random.choice(url_list)
