import datetime
import dashboard
import readWriteFile


def bookReturn():
	print("Enter Name of the book, which you want to return: ")
	bookName = input()
	print("Enter your Name: ")
	borrowerName = input()
	Dtime = datetime.datetime.now()
	writeRow = []
	flag = 0
	# Read the data from BookAvailability.txt
	rows = readWriteFile.readFile('BookAvailability.txt')
	for row in rows:
		if row[3] == borrowerName and row[0] == bookName and row[4] == 'Pending':
			flag = 1
			if Dtime <= datetime.datetime.strptime(row[2], "%d/%m/%Y"):
				row[4] = "Book Returned"
				print("Book Returned Successfully\n\nThank You, Please Visit Again")
				dashboard.updateFileDashboard(bookName, "plus")
			else:
				# Subtracting due date from Returning date(System Generated Time) 
				dateExceed = Dtime - datetime.datetime.strptime(row[2], "%d/%m/%Y")
				penalty = dateExceed.days * 10
				print("Your book has Exceeded Due Date.\nPlease pay the penalty fees, Rs",penalty,"/- to the cash counter.")
				print("\n\nRedirecting to Cash Counter")
				readWriteFile.loading('payment .........', 2)
				print("Payment Done")
				row[4] = "Book Returned"
				print("\n\nBook Returned Successfully")
				dashboard.updateFileDashboard(bookName, "plus")
				print("Thank You, Please Visit Again.")
		writeRow.append(row)

	# Write the data to BookAvailability.txt
	readWriteFile.writeFile('BookAvailability.txt', writeRow, 'w')

	if flag == 0:
		print("\nNo such Book Name/Title found.\nPlease check with the spellings.\nOR\nEnter the value CORRECTLY.")
		bookReturn()

	exit()
