import urllib, urlparse
import random, operator
from collections import defaultdict
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

def is_valid(path):
    if path[:6] != '/wiki/':
        return False

    if path[:10] == '/wiki/File' or \
       'Wikipedia:' in path or \
       'Help:' in path or \
       'Category:' in path or \
       'User:' in path or \
       'talk:' in path or \
       'Special:' in path or \
       'Portal:' in path or \
       'Template:' in path or \
       'International_Standard_Book_Number' in path:
        return False

    return True

def parse_links(url):
    url_list = []
    myopener = MyOpener()
    try:
        #open, read, and parse the text using beautiful soup
        page = myopener.open(url)
        text = page.read()
        page.close()
        soup = BeautifulSoup(text)

        title = soup.find(id='firstHeading').span.text.encode('ascii', 'ignore')
        content = soup.find(id='mw-content-text')
        #find all hyperlinks using beautiful soup
        for tag in content.findAll('a', href=True):
            path = tag['href'].encode('ascii', 'ignore')
            if is_valid(path):
                link = 'http://en.wikipedia.org' + path
                url_list.append(link)
        return title, url_list
    except Exception as e:
        print e
        return None, []

random_url = "http://en.wikipedia.org/wiki/Special:Random"

#parameter to set the number of transitions you make/different pages you visit
num_of_visits = 100

#the url we want to begin with
start_url = random.choice(parse_links(random_url)[1])
current_url = start_url

#dictionary of pages visited so far
visit_history = defaultdict(int)

for i in range(num_of_visits):
    #parsing all the links on the page
    title, url_list = parse_links(current_url)
    print 'Visiting... {0}, url: {1}'.format(title, current_url)

    #incrementing the counts
    visit_history[title] += 1

    #returning a random link to go to
    if len(url_list) == 0:
        print 'No links found, starting at beginning page'
        current_url = start_url
    else:
        current_url = random.choice(url_list)

visits = [(url, visit_history[url]) for url in visit_history if visit_history[url] > 2]
sorted_visits = sorted(visits, key=operator.itemgetter(1))

print 'started at: ' + start_url
print sorted_visits
