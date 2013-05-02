__author__ = 'zfei'

import urllib2
# from bs4 import BeautifulSoup
from pymongo import MongoClient
from twitterCrawler import twitterCrawler
import os
import demjson

import signal
import sys
import socket
import time

class myRun:
    def __init__(self):
        self.curr = 0

        self.start_idx= 0
        self.end_idx = 0
        self.errorlist =[]

    def getList(self):
        cc = 0
        ins = open("data/json.txt","r")
        ret = []
        strs = []
        for line in ins:
            line = line.strip()
            if not len(line) == 0:
                obj = demjson.decode(line)
                ret.append(obj)

        return ret






    def run(self, lastsave=0):

        self.curr = lastsave
        print "Reading file, Please wait... "
        users = self.getList()

        print "-----------------------"

        print "Last time end at ", str(lastsave)

        if str(lastsave)=="0":
            self.start_idx = raw_input("Please select your START index: (0 ~ "+ str(len(users)-1)  + "):\n")
            self.end_idx = raw_input("Please select your ENDT index: (0 ~ "+  str(len(users)-1)+ "):\n")
            self.start_idx = int(self.start_idx)
            self.end_idx = int(self.end_idx)
        else:
            self.start_idx = int(lastsave)
            self.end_idx = self.start_idx+500


        print "Total ", str(int(self.end_idx)-int(self.start_idx))
        for i in range(self.start_idx,self.end_idx):
            try:
                if i%2==0:
                    time.sleep(0.5)
                ins = users[i]


                uid = ins['user_id']
                un = ins['USER_NAME']
                tc = twitterCrawler(un, str(uid) )
                tc.pull()
                tc.writeFile()
                self.curr = i
                print self.curr

            except Exception, e:
                sys.stderr.write("Failed at file "+str(i)+"\n")
                ins = users[i]
                uid = ins['user_id']
                self.errorlist.append(uid)





def loadSt():
    # uname = os.getlogin()
    uname = socket.gethostname()

    filename = "save_"+uname+".txt"
    ins = open(filename,"r")
    data = []
    for line in ins:
        data.append(line)
    ins.close()
    for line in data:
        return int(line.strip())



def saveSt():
    # uname = os.getlogin()
    uname = socket.gethostname()

    filename = "save_"+uname+".txt"
    ins = open(filename,"w")
    ins.write(str(ooo.curr))
    ins.close()

    filename = "err_"+uname+".txt"
    ins = open(filename,"a")
    for line in ooo.errorlist:
        ins.write(str(line)+"\n")
    ins.close()



def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    print 'Start from index', ooo.start_idx
    print 'end at index', ooo.curr

    # save end profile:
    saveSt()

    sys.exit(0)



signal.signal(signal.SIGINT, signal_handler)
try:
    lr = loadSt()
except Exception, e:
    lr =0

ooo = myRun();
ooo.run(lastsave=lr)
saveSt()
