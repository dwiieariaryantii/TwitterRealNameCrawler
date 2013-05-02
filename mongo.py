__author__ = 'haowu'
from pymongo import MongoClient
from pymongo import Connection



ins = open("data/list_of_users_that_have_tweets.txt","r")

datas = [];
for line in ins:
    datas.append(line)
ins.close()

# ins = open("data/list_of_users_that_have_tweets.txt","r")
connection = Connection()
db = connection.test
# col = db.tweet_data


to_write = []
for line in datas:
    try:
        sc = db.tweet_data.find_one({'user_id': int(line)})['USER_NAME'];
        obj ={}
        obj["user_id"]=int(line)
        obj["USER_NAME"] = sc
        print str(obj)
        to_write.append(obj)
    except KeyError:
        # print db.tweet_data.find_one({'user_id': int(line)})
        pass
#
# ins = open("data/parsed.txt","w")
# for d in to_write:
#     ins.write(d+"\n")
# ins.close()




