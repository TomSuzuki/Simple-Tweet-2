import os
import sys
import json

AccountID = "0x0553"

UserIDPath = os.getenv('HOMEDRIVE') + os.getenv('HOMEPATH') + '\\OneDrive\\ドキュメント\\Twitter\\TwitterKey.json'
temp = open(UserIDPath, 'r')
UserIDData = json.load(temp)

ConsumerKey = UserIDData[AccountID]['ConsumerKey']

print(ConsumerKey)

