import csv
from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获取日期，最高气温和最低气温
filename1 = 'sitka_weather_2014.csv'
filename2 = 'death_valley_2014.csv'

with open(filename1) as f_o:
    reader = csv.reader(f_o)
    header_row = next(reader)

##    for index, column_header in enumerate(header_row):
##        print(index, column_header)
    dates = [ ]
    highs = [ ]
    lows  = [ ]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])  
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            

#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#设置图形的格式
plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate( )    #绘制斜的日期标签
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


with open(filename2) as f_o2:
    reader = csv.reader(f_o2)
    header_row = next(reader)

##    for index, column_header in enumerate(header_row):
##        print(index, column_header)
    dates = [ ]
    highs = [ ]
    lows  = [ ]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])  
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            

#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#设置图形的格式
plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate( )    #绘制斜的日期标签
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show( )
