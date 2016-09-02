#!/usr/bin/env python

import sys, json, re, itertools

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
    
    #iterate through the tweets
    tweetSentiment = []
    for tweet in tweets:
        if u'text' in tweet:
            tweetText = tweet[u'text']
        else:
            tweetSentiment.append(0)
            continue
        
        sentiment = 0
        words = re.findall(r"\w+", tweetText)
        for word in words:
            if word in sentiments:
                sentiment += sentiments[word]
        tweetSentiment.append(sentiment)
    
    #create a list of words that are not in the sentiment file, but in our tweets
    newWords = {}
    for tweet in tweets:
        if u'text' in tweet:
            tweetText = tweet[u'text']
        else:
            continue
        words = re.findall(r"\w+", tweetText)
        for word in words:
            if word not in sentiments:
                newWords[word] = {"positiveTotal": 0, "negativeTotal": 0, "count": 0}
    
    #iterate through tweets again, this time adding to positiveTotal and negativeTotal 
    #for each word in each tweet
    for tweet, sentiment in itertools.izip(tweets, tweetSentiment):
        if u'text' in tweet:
            tweetText = tweet[u'text']
        else:
            continue
        words = re.findall(r"\w+", tweetText)
        for word in words:
            if word not in sentiments:
                newWords[word]["count"] += 1
                if sentiment >= 0:
                    newWords[word]["positiveTotal"] += sentiment
                else:
                    newWords[word]["negativeTotal"] += sentiment
    
    #assign a sentiment to each word according to a formula
    for word in newWords:
        positiveTotal = newWords[word]["positiveTotal"]
        negativeTotal = newWords[word]["negativeTotal"]
        try:
            import math
            newWords[word]["sentiment"] = float(positiveTotal + negativeTotal)/float(positiveTotal - negativeTotal)
        except ZeroDivisionError:
            newWords[word]["sentiment"] = 0
    
    sortedWords = [(x, newWords[x]["sentiment"]) for x in newWords]
    sortedWords.sort(key=lambda pair: pair[1], reverse=True)
    
    for pair in sortedWords:
        print pair[0] + " " + str(pair[1])

if __name__ == '__main__':
    main()
