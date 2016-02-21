import json
import sys
import re

def hw(sent_file, tweet_file):
    afinnfile = sent_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    tweets = {}
    new_words = []
    for line in tweet_file:
        tweet_dict = json.loads(line)
        text = ''
        if 'text' in tweet_dict:
            text = tweet_dict['text'].encode('utf-8')
        #The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.
        terms = re.findall(r"[\w']+", text)
        terms_sum = 0
        for term in terms:
            if term in scores:
                terms_sum += scores[term]
            else:
                new_words.append(term)
        tweets[text] = terms_sum

    for word in new_words:
        pos = neg = total = 0

        for tweet in tweets:
            if word in tweet:
                if tweets[tweet]>0:
					pos+=1
                elif tweets[tweet]<0:
                    neg+=1
            	total+=1

		print word, ' ', (pos - neg)/total

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
