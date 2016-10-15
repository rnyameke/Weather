# Weather
## Purpose
Script that takes a start and end date and pulls temperature from weather underground API.

##Before running
- Generate API key from wunderground.com/api and replace "your_api_key" in url with the generated API key
- If fetching temperature data for more than 10 days, uncomment the sleep function towards the bottom of the code. Weather Underground only allows 10 queries per minute for their free plan.

##Output
A csv file is created with the date, time and temperature for the 53rd minute of every hour. This is because some days have multiple temperature values per hour, and the 53rd minute is the most commonly recorded one. Note that some hours do not have any temperature recorded, and those hours will be skipped with no warning.

##Sources
Obtained help from some posts in StackOverflow for the date iterator.
