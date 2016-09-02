#!/usr/bin/env python

import sys, json

def main():
    tweets_file = open("/Users/adam/Projects/uw-data-manipulation/assignment1/large_output.txt")
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
    for hashtag in hashtagList:
        try:
            print str(hashtag[0]) + " " + str(hashtag[1])
        except UnicodeEncodeError:
            continue
            
if __name__ == '__main__':
    main()
    
    