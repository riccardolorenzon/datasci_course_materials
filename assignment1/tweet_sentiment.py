import json
import sys
import re

def hw(sent_file, tweet_file):
    afinnfile = sent_file
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        tweet_dict = json.loads(line)
        text = ''
        if 'text' in tweet_dict:
            text = tweet_dict['text'].encode('utf-8')
        else:
            print line
        #The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.
        terms = re.findall(r"[\w']+", text)
        terms_sum = 0
        for term in terms:
            if term in scores:
                terms_sum += scores[term]
        print terms_sum

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
