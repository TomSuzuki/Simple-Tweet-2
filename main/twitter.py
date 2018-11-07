import os
import sys
import json
from twitter import *

# 終了動作
def EscapeKey(event):
    print('終了コマンドが送られました。')
    sys.exit()

# 実行動作
def fn_Tweet(tt):
    TweetMessage = tt
    t = Twitter(auth=OAuth(AccessToken, AccessTokenSecret, ConsumerKey, ConsumerSecret))
    t.statuses.update(status=TweetMessage)
    print("success")
    sys.exit()

if __name__ == '__main__':
    # 取得＆設定
    UserIDPath = os.getenv('HOMEDRIVE') + os.getenv('HOMEPATH') + '\\OneDrive\\ドキュメント\\Twitter\\TwitterKey_0x0553.json'
    temp = open(UserIDPath, 'r')
    UserIDData = json.load(temp)
    UserID = UserIDData['UserID']
    ConsumerKey = UserIDData['ConsumerKey']
    ConsumerSecret = UserIDData['ConsumerSecret']
    AccessToken = UserIDData['AccessToken']
    AccessTokenSecret = UserIDData['AccessTokenSecret']

    # 入力処理
    TweetMessage = input("Please Enter Tweet: ")
    fn_Tweet(TweetMessage)
    



