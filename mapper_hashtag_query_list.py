#!/usr/bin/env python

import json as js
import sys


'''
*** You can change the HASHTAG_LIST to search for hashtags,
*** or you can change the USER_LIST to search for users mentioned.
'''

## THESE ARE HASHTAGS TO SEARCH FOR
HASHTAG_LIST = ['guncontrolnow','guncontrol','massshooting','gun','2ndamendment','stayinmylane','columbine','triggerchange','gunviolence',\
'sandyhook','NRA','schoolshooting','gunsense', 'MarchForOurLives','2a','gunlaws','notonemore','everytown','bumpstock','bumpstockban',]

## THESE ARE TWITTER USER NAMES TO SEARCH FOR
USER_LIST = ['NRA','everytown','GOP','TheDemocrats']



## DO NOT CHANGE ANY OF THE CODE BELOW:
ulist = USER_LIST
hlist = HASHTAG_LIST
for dat in sys.stdin:
  next_line = False
  try:
    ln = js.loads(dat)
  except ValueError:
    continue
  try:
    entities = ln['entities']
    hashtags = entities['hashtags']
    user_mentions = entities['user_mentions']
  except KeyError:
    continue
  for hashtag in hashtags:
    try:
      hashtag = hashtag['text']
      hashtag = hashtag.lower()
      for term in hlist:
        term = term.strip()
        if term in hashtag: 
          try:
            print dat
            next_line = True
            break
          except KeyError:
            continue
    except UnicodeEncodeError:
      continue
  if next_line == True:
    continue
  for user in user_mentions:
    try:
      screen_name = user['screen_name']
      screen_name = screen_name.lower()
      for term in ulist:
        term = term.strip()
        if term == screen_name:
          print dat
          next_line = True
          break
    except KeyError:
      continue
  if next_line == True:
    try:
      rtweet = ln['retweet_status']
      rtuser = rtweet['user']
      rt_screen_name = rtuser['screen_name']
      rt_screen_name = rt_screen_name.lower()
      for term in ulist:
        term = term.strip()
        if term == rt_screen_name:
          print dat
    except KeyError:
      continue


