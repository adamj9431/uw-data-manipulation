#!/usr/bin/env python

import sys, json

def main():
    tweets_file = open(sys.argv[1])
    tweets = []
    for line in tweets_file:
        try:
            tweet = json.loads(line.lower(), strict=False)
            tweets.append(tweet)
        except ValueError as e:
            continue
    tweets_file.close()
    allHashtags = {}
    for tweet in tweets:
        if (('entities' not in tweet) 
                    or ('hashtags' not in tweet['entities']) 
                    or len(tweet['entities']['hashtags'])==0):
            continue
        tweetHashtags = [x['text'] for x in tweet['entities']['hashtags']]
        for hashtag in tweetHashtags:
            allHashtags[hashtag] = 1 + allHashtags.get(hashtag, 0)

    hashtagList = allHashtags.items()
    hashtagList.sort(key=lambda k: k[1], reverse=True)
    hCount = 0
    for hashtag in hashtagList:
        try:
            print str(hashtag[0]) + " " + str(hashtag[1])
            hCount += 1
            if (hCount == 10):
                break
        except UnicodeEncodeError:
            continue
            
if __name__ == '__main__':
    main()
    
    