import csv
import sys
import time



def readFile(fileName):
	with open(fileName) as csv_file:
		csv_reader = list(csv.reader(csv_file, delimiter=','))
		return csv_reader


def writeFile(fileName, writeRow, modd):
	with open(fileName, mode=modd) as csv_file:
		csv_writer = csv.writer(csv_file, delimiter = ',')
		for row in writeRow:
			csv_writer.writerow(row)


def loading(content, t):
	lspeed = 4
	loadstring = content * 1
	i = 0
	while i < t:
	    for index, char in enumerate(loadstring):
	        sys.stdout.write(char)
	        sys.stdout.flush()
	        time.sleep(1.0 / lspeed) 
	    index += 1
	    i += 1
	    sys.stdout.write("\b" * index + " " * index + "\b" * index)
	    sys.stdout.flush()
	sys.stdout.flush()