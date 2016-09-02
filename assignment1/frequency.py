import sys, json, re

def main():
    tweets_file = open(sys.argv[1])
    
    tweets = []
    for line in tweets_file:
        try:
            tweet = json.loads(line.lower(), strict=False)
            tweets.append(tweet)
        except ValueError as e:
            print str(type(line)) + '\n' + str(e) + '\n' + line
    
    allWords = {}
    totalWords = 0.0
    for tweet in tweets:
        if u'text' in tweet:
            tweetText = tweet[u'text']
        else:
            continue

        import re
        words = re.findall(r"\w+", tweetText)
        for word in words:
            totalWords += 1.0
            if word not in allWords:
                allWords[word] = 1
            else:
                allWords[word] += 1
    
    for word in allWords:
        allWords[word] = float(allWords[word])/totalWords
    
    sortedWords = sorted(allWords.items(), key=lambda a: a[1], reverse=True)
    
    for word in sortedWords:
        print word[0] + " " + str(word[1])

if __name__ == '__main__':
    main()