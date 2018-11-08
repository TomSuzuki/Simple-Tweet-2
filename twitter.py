import os
import sys
import json
from twitter import *

# 実行動作
def fn_Tweet(p1,p2):
	# アカウント
	AccountID = p2
	
	# 取得＆設定
	UserIDPath = os.getenv('HOMEDRIVE') + os.getenv('HOMEPATH') + '\\OneDrive\\ドキュメント\\Twitter\\TwitterKey.json'
	temp = open(UserIDPath, 'r')
	UserIDData = json.load(temp)
	ConsumerKey = UserIDData[AccountID]['ConsumerKey']
	ConsumerSecret = UserIDData[AccountID]['ConsumerSecret']
	AccessToken = UserIDData[AccountID]['AccessToken']
	AccessTokenSecret = UserIDData[AccountID]['AccessTokenSecret']
	
	# ツイート
	TweetMessage = p1
	t = Twitter(auth=OAuth(AccessToken, AccessTokenSecret, ConsumerKey, ConsumerSecret))
	t.statuses.update(status=TweetMessage)
	print("success")
	sys.exit()

if __name__ == '__main__':
	# 入力処理
	AccountID = input("Please Enter UserID: ")
	TweetMessage = input("Please Enter Tweet: ")
	if(TweetMessage == ""):
		print("exit")
		sys.exit()
	fn_Tweet(TweetMessage,AccountID)




