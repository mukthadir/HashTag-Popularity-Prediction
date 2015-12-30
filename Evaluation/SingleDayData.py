import json
import re

inputFile = 'SPOWS'

# Loading the input json file for reading it
tweets = []
for line in open(inputFile, 'r'):
    tweets.append(json.loads(line))

# Finding the most recent and the oldest tweet's timestamp
minimum_timestamp = tweets[0]['timestamp']

day_10 = 864000000
day_15 = 1296000000
day_20 = 1728000000

# taking the data till 20th day from the starting
min_ts = minimum_timestamp + day_10
max_ts = min_ts + 3600000

# iterating through all the tweets and saving all the relevant data
my_array = dict()
for tweet in tweets:
    days = 0
    timestamp = tweet['timestamp']
    if(timestamp < max_ts):
        if(timestamp > min_ts):
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
                        days = 0
                    days += 1

                    # saving the occurence of hashtag with the hashtag name in a dictionary
                    my_array[value] = days


# list to keep the hashtags that would appear in future tweets
final_list = list()

# Predicting the popularity of hashtag in the next one hour
for hashtag in my_array:
    freq_each_day = my_array[hashtag]
    final_list.append((hashtag, freq_each_day))


# sorting the final list to obtain the hashtags that would appear the most
final_list = sorted(final_list, key= lambda x: x[1], reverse= True)

out = 'ActualHashtags11thDay.csv'
f = open(out, 'w')
for val in final_list:
    f.write(str(val[0]) + ', ' + str(int(val[1])) + '\n')
f.close()
