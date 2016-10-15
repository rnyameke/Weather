import urllib2
import json
import time
import csv
from datetime import date, datetime as dt, timedelta as td

#url prefix for querying
site = 'http://api.wunderground.com/api/your_api_key/history_'
city ='/q/OH/Cleveland.json'

#creating the date range
start_date = date(2015, 1, 1)
end_date = date(2015, 1, 5)
date_range = end_date - start_date

dates = []

#loops through from the start date to the end date
for i in range(date_range.days + 1):
    dates.append (dt.strptime(str(start_date  + td(days=i)), '%Y-%m-%d').strftime('%Y%m%d'))
    i = i+1

#column names
colnames = ["Date","Time", "Temp"]

#initializing variables
temps = []
obs_date = []
date_only = []
time_only = []

for date in dates:
    #build url
    url = site + date + city

    #grab json and parse
    f = urllib2.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    #f.close()

    #grab the date, time and temperature reading for each hour, at the 53rd minute (most commonly occurring minute)
    for j in parsed_json['history']['observations']:
        if int(j['date']['min']) == 53:
            obs_date=(dt(int(j['date']['year']),int(j['date']['mon']),int(j['date']['mday']), int(j['date']['hour']), int(j['date']['min'])))
            date_only.append (dt.strftime(obs_date, '%Y-%m-%d'))
            time_only.append (obs_date.time())
            temps.append(j['tempi'])
    #time.sleep(6)

#combine the lists of dates, times and temps
values = zip(date_only, time_only, temps)

#open file
with open('test.csv', 'wb') as out:
    writer = csv.writer( out )

    #write headers
    writer.writerow(colnames)

    #write the csv file
    for value in values:
        writer.writerow(value)
