#!/usr/bin/env python

import sys, json, re

def main():
    sentiment_file = open(sys.argv[1])
    tweets_file = open(sys.argv[2])

    #get sentiments into a dictionary
    sentiments = {}
    for line in sentiment_file:
        term, score = line.split('\t')
        sentiments[term] = int(score)
    sentiment_file.close()

    #get tweets into a list
    tweets = []
    for line in tweets_file:
        tweet = json.loads(line.lower(), strict=False)
        tweets.append(tweet)

    tweets_file.close()
    
    #iterate through the tweets and print a sentiment for each one
    for tweet in tweets:
        if u'text' in tweet:
            tweetText = tweet[u'text']
        else:
            print 0
            continue
        
        sentiment = 0
        words = re.findall(r"\w+", tweetText)
        for word in words:
            if word in sentiments:
                sentiment += sentiments[word]
        print sentiment
    
    

if __name__ == '__main__':
    main()
