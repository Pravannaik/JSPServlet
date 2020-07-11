import readWriteFile
import borrow
import re


column_Names = []
row_lists = []
books = []
magazines = []
journals = []



def updateFileDashboard(bName, action):
	temp = []
	rows = readWriteFile.readFile('Materials.txt')
	for row in rows:
		if row[0] == bName:
			if action == 'plus':
				row[5] = int(row[5]) + 1
			else:
				row[5] = int(row[5]) - 1
		temp.append(row)

	readWriteFile.writeFile('Materials.txt', temp, 'w')




def displayRows(search, action):
	rows = readWriteFile.readFile('Materials.txt')
	i = 0
	flag = 0
	for row in rows:
		if i == 0:
			print("Sr.No|","|".join(row))
			i += 1
		else:
			if re.findall(action, row[search]):#for match case
			# if row[search] == action:
				print(i,"|","|".join(row))
				i += 1
				flag = 1
	if flag == 0:
		print("No Records Found")




def borrowSearch():
	#Title name should be same as on the book
	print("\nEnter the Name of the book, you want to Borrow.\nOR\nFilter (Press * for Search using filter.\nOR\nPress 0 to EXIT")
	response = input()
	if response == '*':
		search()
	elif response == '0':
		exit()
	else:
		print("You have entered :",response)
		print("Please wait")
		readWriteFile.loading('checking ...........', 4)
		borrow.checkBook(response)




def searchDasboard():
	print("\n****************Search Dashboard****************")




def search():
	print("Choose one option.\nSearch By:")
	print("1. Title\t2. Author\t3. ISBN Number\t4. Subject")
	search = int(input())
	if search == 1:
		print("\nYou have selected Search By Title.\nEnter the Title :")
		title = input()
		readWriteFile.loading('searching .........', 3)
		searchDasboard()
		displayRows(search - 1, title)
		borrowSearch()
	elif search == 2:
		print("\nYou have selected Search By Author.\nEnter the Author :")
		author = input()
		readWriteFile.loading('searching .........', 3)
		searchDasboard()
		displayRows(search - 1, author)
		borrowSearch()
	elif search == 3:
		print("\nYou have selected Search By ISBN Number.\nEnter the ISBN Number :")
		isbn = input()
		readWriteFile.loading('searching .........', 3)
		searchDasboard()
		displayRows(search - 1, isbn)
		borrowSearch()
	elif search == 4:
		print("\nYou have selected Search By Subject.\nEnter the Subject :")
		sub = input()
		readWriteFile.loading('searching .........', 3)
		searchDasboard()
		displayRows(search - 1, sub)
		borrowSearch()
	else:
		print("\nYou have entered the wrong value.\nPlease select CORRECTLY.")
		search()




def display():
	print("\n****************Display Dashboard****************")
	s = 4
	print("\nBooks Section")
	displayRows(s, "Book")
	print("\nMagazines Section")
	displayRows(s, "Magazines")
	print("\nJournals Section")
	displayRows(s, "Journals")
	borrowSearch()

