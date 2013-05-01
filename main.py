__author__ = 'zfei'

import urllib2
from bs4 import BeautifulSoup
from pymongo import MongoClient

def pull(screen_name):
    page = urllib2.urlopen("https://twitter.com/" + screen_name)
    soup = BeautifulSoup(page)
    print soup.select("span.profile-field")[0].string

def update_each_user(collection):


def main():
    db = MongoClient().tweet_data
    collection = db.tweet_data
    cursor = collection.find(tailable=True)

main()