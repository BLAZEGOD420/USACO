"""
ID: howieen1
LANG: PYTHON3
TASK: friday
"""

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

years = int(fin.readline()) + 1899

monthsList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0
weekDict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
def isLeap(year):
	if year % 400 == 0:
		return True
	elif ((year % 4) == 0) and ((year % 100) != 0):
		return True
for year in range(1900, years + 1):
	for month in range(12):
		if month == 1 and isLeap(year):
			monthsList[1] = 29
		else:
			monthsList[1] = 28
		for day in range(1, monthsList[month] + 1):
			days += 1
			if day == 13:
				if ((days - 1) % 7) == 0:
					weekDict[0] += 1
				if ((days - 2) % 7) == 0:
					weekDict[1] += 1
				if ((days - 3) % 7) == 0:
					weekDict[2] += 1
				if ((days - 4) % 7) == 0:
					weekDict[3] += 1
				if ((days - 5) % 7) == 0:
					weekDict[4] += 1
				if ((days - 6) % 7) == 0:
					weekDict[5] += 1
				if ((days - 7) % 7) == 0:
					weekDict[6] += 1

				
out = str(weekDict[5]) + ' ' + str(weekDict[6]) + ' ' + str(weekDict[0]) + ' ' + str(weekDict[1]) + ' ' + str(weekDict[2]) + ' ' + str(weekDict[3]) + ' ' + str(weekDict[4])
fout.write(out + '\n')
fout.close()
			
	

