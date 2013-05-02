__author__ = 'haowu'


from bs4 import BeautifulSoup
from pymongo import MongoClient
import urllib2
import json

class twitterCrawler:
    def __init__(self, screen_name,uid):
        self.screen_name = screen_name
        self.uid = uid

    def pull(self):
        # self.findSCName()
        # print "https://twitter.com/" + self.screen_name
        page = urllib2.urlopen("https://twitter.com/" + self.screen_name)
        soup = BeautifulSoup(page)
        self.fullName =  soup.find('span',{'class':'profile-field'}).string.strip();
        self.webside = soup.select("span.url.editable-group")[0].find('a').string.strip();


    def writeFile(self):
        profile = {}
        profile['user_id'] = int(self.uid)
        profile['USER_NAME'] = self.screen_name
        profile['FULL_NAME'] = self.fullName
        profile['WEBSITE'] = self.webside

        ins = open("output/"+self.uid,"w")
        js = json.dumps(profile)

        ins.write(str(js) )
        ins.close()




    # def findSCName(self):
    #     self.screen_name = "bbc"
    #     db = MongoClient().tweet_data
    #     collection = db.tweet_data
    #     cursor = collection.find(tailable=True)
