#!/usr/bin/python

import time
import bs4
import urllib2
from pprint import pprint

def download_page(url):
    retry = 0
    while retry < 5:
        try:
            print "Downloading", url
            return bs4.BeautifulSoup(urllib2.urlopen(url).read())
            break
        except urllib2.HTTPError, e:
            print "Failed to get", repr(url), "retrying"
            retry += 1
        except:
            print "Failed to get", repr(url)
            raise
    else:
        raise IOError("Failed to get %r", url)

page = download_page("https://www.crowdsupply.com/numato-lab/opsis")
project = page.find('section', attrs={'class':'section-project'})

facts = [" ".join(fact.text.split()).strip() for fact in project.findAll(attrs={'class': 'fact'})]

left, percent_funded, pledges = facts

pledged = project.find(attrs={'class': 'project-pledged'}).text.strip()
goal = project.find(attrs={'class': 'project-goal'}).text.strip()

print ",".join([str(time.time()), pledged, goal, left, percent_funded, pledges])

data={
  'time': time.time(), 
  'pledged': int(pledged.split()[0][1:].replace(',', '')),
  'goal': int(goal.split()[1][1:].replace(',', '')), 
  'percent_funded': int(percent_funded.split()[0][:-1]),
  'pledges': int(pledges.split()[0])}
print data

scraperwiki.sqlite.save()
