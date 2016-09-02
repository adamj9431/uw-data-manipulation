#!/usr/bin/env python

import sys, json, re

states = {
    'ak': 'alaska',
    'al': 'alabama',
    'ar': 'arkansas',
    'as': 'american samoa',
    'az': 'arizona',
    'ca': 'california',
    'co': 'colorado',
    'ct': 'connecticut',
    'dc': 'district of columbia',
    'de': 'delaware',
    'fl': 'florida',
    'ga': 'georgia',
    'gu': 'guam',
    'hi': 'hawaii',
    'ia': 'iowa',
    'id': 'idaho',
    'il': 'illinois',
    'in': 'indiana',
    'ks': 'kansas',
    'ky': 'kentucky',
    'la': 'louisiana',
    'ma': 'massachusetts',
    'md': 'maryland',
    'me': 'maine',
    'mi': 'michigan',
    'mn': 'minnesota',
    'mo': 'missouri',
    'mp': 'northern mariana islands',
    'ms': 'mississippi',
    'mt': 'montana',
    'na': 'national',
    'nc': 'north carolina',
    'nd': 'north dakota',
    'ne': 'nebraska',
    'nh': 'new hampshire',
    'nj': 'new jersey',
    'nm': 'new mexico',
    'nv': 'nevada',
    'ny': 'new york',
    'oh': 'ohio',
    'ok': 'oklahoma',
    'or': 'oregon',
    'pa': 'pennsylvania',
    'pr': 'puerto rico',
    'ri': 'rhode island',
    'sc': 'south carolina',
    'sd': 'south dakota',
    'tn': 'tennessee',
    'tx': 'texas',
    'ut': 'utah',
    'va': 'virginia',
    'vi': 'virgin islands',
    'vt': 'vermont',
    'wa': 'washington',
    'wi': 'wisconsin',
    'wv': 'west virginia',
    'wy': 'wyoming'
}


def main():
    tweets_file = open(sys.argv[2])
    tweets = []
    for line in tweets_file:
        try:
            tweet = json.loads(line.lower(), strict=False)
            tweets.append(tweet)
        except ValueError as e:
            continue
    tweets_file.close()
    sentiment_file = open(sys.argv[1])
    sentiments = {}
    for line in sentiment_file:
        term, score = line.split('\t')
        sentiments[term] = int(score)
    sentiment_file.close()
    
    stateSentiments = {}
    for tweet in tweets:
        if ('text' not in tweet) or ('user' not in tweet) or tweet['user']['location'] is None:
            continue
        tweetText = tweet[u'text']
        sentiment = 0
        words = re.findall(r"\w+", tweetText)
        for word in words:
            if word in sentiments:
                sentiment += sentiments[word]
        try:
            rawLocation = str(tweet['user']['location'].lower())
        except UnicodeEncodeError:
            continue
        
        matched = False
        for stateAbbrev in states:
            if (rawLocation.endswith(" " + stateAbbrev) or rawLocation.endswith("," + stateAbbrev)):
                matched = True
                break
            elif (states[stateAbbrev] in rawLocation):
                matched = True
                break
    
        if not matched:
            continue
    
        if stateAbbrev not in stateSentiments:
            stateSentiments[stateAbbrev] = {'totalSentiment': 0, 'count': 0}
        stateSentiments[stateAbbrev]['totalSentiment'] += sentiment
        stateSentiments[stateAbbrev]['count'] += 1
    
    for stateAbbrev in stateSentiments:
        count = stateSentiments[stateAbbrev]['count']
        total = stateSentiments[stateAbbrev]['totalSentiment']
        stateSentiments[stateAbbrev]['averageSentiment'] = float(total)/float(count)
    
    stateList = stateSentiments.items()
    stateList.sort(key=lambda s: s[1]['averageSentiment'], reverse=True)
    print stateList[0][0].upper()

if __name__ == '__main__':
    main()
    
    
    