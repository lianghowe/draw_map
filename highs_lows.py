import csv

from matplotlib import pyplot as plt 
from datetime import datetime

# 从文件中获取最高气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	highs, dates, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], 
				"%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)


			#high = int(row[1])
			highs.append(high)

			#low = int(row[3])
			lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi = 128, figsize = (10, 6))
plt.plot(dates, highs, c = 'red', alpha=  0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', 
	alpha = 0.1)

# 设置图形的格式
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize = 20)
	
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperatures (F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', 
	labelsize = 16)

plt.show()