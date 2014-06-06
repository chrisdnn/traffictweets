import string
import json

class M_tweetsDAO(object):
#initialize with database and set mongodb collection to use
	def __init__(self, database):
		self.db = database
		self.db.tweets = database.tweets

#finding of tweets
	def find_tweets(self):
		l = []
		for each_name in self.db.tweets.find():
			l.append({'name':each_name['name'], 'email':each_name['email']})
		return l

#insertion of tweets
	def insert_tweet(self, tdata):
                 print('DAO_text:' + json.dumps(tdata["text"]))
                 self.db.tweets.insert(tdata)
#                if tdata[0].isdigit():pass                else:                        self.tweetsdb.insert(json.loads(tdata))

