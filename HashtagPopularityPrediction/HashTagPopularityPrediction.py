import json
import re

inputFile = 'SPOWS'

# Loading the input json file for reading it
tweets = []
for line in open(inputFile, 'r'):
    tweets.append(json.loads(line))

# Finding the most recent and the oldest tweet's timestamp
minimum_timestamp = tweets[0]['timestamp']
maximum_timestamp = tweets[-1]['timestamp']

# determining the interval of data we have
interval = (maximum_timestamp - minimum_timestamp)

# dividing the total interval into multiple fragments
window = interval/25

days = [0]*25

# taking the data till 20th day from the starting
#max_ts = minimum_timestamp + 1728000000

# iterating through all the tweets and saving all the relevant data
my_array = dict()
for tweet in tweets:
    timestamp = tweet['timestamp']
#    if(timestamp < max_ts):
    keywords_array = tweet['keywords']
    for value in keywords_array:
        if(value[0] == '#'):
            # cleaning the input tweets and changing to ascii characters by removing the 
            # non-ascii characters
            value = re.sub('[!@#$,.:;/?><}{=+-_)(*&^%)}]', '', value)
            value = value.encode('ascii','ignore')

            # checking if the hashtag was already used before in another tweet or not
            if(value in my_array):
                 days = my_array[value]
            else:
                days = [0]*25

            # saving the hashtag in the particular day it had appeared
            for i in range(1, len(days) + 1):
                minn = minimum_timestamp + (i*window)
                maxx = minimum_timestamp + (i+1)*window

                if(timestamp > minn and timestamp < maxx):
                    days[i-1] += 1

            # finally saving the occurence of hashtag with the hashtag name in a dictionary
            my_array[value] = days


# list to keep the hashtags that would appear in future tweets
final_list = list()

# Predicting the popularity of hashtag in the next one hour
for hashtag in my_array:
    freq_each_day = my_array[hashtag]

    popularity = 0
    for i in range(0, 25):
        delta = (i+1) * 0.02
        popularity += freq_each_day[i]*delta
    # pop = freq[0]*0.1 + freq[1]*0.2 + freq[2]*0.3 + freq[3]*0.4 + freq[4]*0.5
    popularity = popularity/32
    final_list.append((hashtag, popularity))


# sorting the final list to obtain the hashtags that would appear the most
final_list = sorted(final_list, key= lambda x: x[1], reverse= True)


out = 'PredictedPopularityOfHashtags.csv'
f = open(out, 'w')
for val in final_list:
    f.write(str(val[0]) + ', ' + str(int(val[1])) + '\n')
f.close()
