HashtagPopularityPrediction folder contains the code that predicts the hashtags that would be most popular in the next one hour along with their counts of usage by people all over the world.

1. Run HashTagPopularityPrediction.py in terminal. This will generate PredictedPopularityOfHashtags.csv file which will contain the result. The hashtags are arranged in decreasing order


Evaluations are placed under Evaluation folder.

2. Run HashTagPredictionTestModel.py in terminal. This produces 3 different results. By default, this calculates the hashtags for first 10 days.
3. For obtaining the prediction for 15 days and 20 days, please open HashTagPredictionTestModel.py and change line number 29 and instead of day_10, write day_15 and day_20 respectively.

This file gives the predicted hash tag values of different data sets.

4. Run SingleDayData.py in terminal. This produces 3 different results. By default, this calculates the hashtags that are being used by people in the 1st hour of 11th day.
5. For obtaining the values for 1st hour of 16th day and 21st day, please open SingleDayData.py and change the line number 19 and instead of day_10, write day_15 and day_20, respectively.

6. RMSECalculator.py calculates the RMSE values for predicted and actual hashtag frequencies. By default, this calculates the RMSE values for 10 days.
7. To obtain the RMSE values of 15 days and 20 days, please open the file and change the line number 18 and 19 and instead of actual_10_days and expected_10_days, you need to write actual_15_days and expected_15_days and actual_10_days and expected_10_days, respectively.
