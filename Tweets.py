import snscrape.modules.twitter as sntwitter
import csv
maxTweets = 250

csvFile = open('Tweets.csv', 'a', newline='', encoding='utf8')

csvWriter = csv.writer(csvFile)
csvWriter.writerow(['text'])


for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:@Steve_Dangle + since:2021-11-12 until:2021-11-16-filter:replies Leafs').get_items()):
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.content,tweet.id,tweet.username,tweet.date,tweet.url])
csvFile.close()
