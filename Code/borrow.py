import datetime
import main
import dashboard
import readWriteFile




def checkForMembership(fName, lName):
	flag = 0
	count = 0
	rows = readWriteFile.readFile('NewMember.txt')
	for row in rows:
		if row[0] == fName and row[1] == lName:
			flag = 1
			checkRows = readWriteFile.readFile('BookAvailability.txt')
			for chkrow in checkRows:#member can avail 2 book check
				if chkrow[3] == fName and chkrow[4] == 'Pending':
					count += 1 

	if count == 2:
		print("\nSorry, Only 2 books can avail per Member.\nYou have already issued 2 books.")
		print("Thank You")
		exit()

	if flag == 0:
		print("\nYou are not availed for Membership\nPlease be a Member first.\nThank You.")
		print("\n\nExiting to Main Page.")
		readWriteFile.loading('exiting ..........', 2)
		main.main()



def borrowBook(titleName):
	print("Do you want to borrow this book (Y/N):")
	res = input()
	if res == 'Y':
		print("Please Enter your First Name: ")
		name = input()
		print("Please Enter your Last Name: ")
		last = input()
		print("Checking Membership")
		readWriteFile.loading('checking ..........', 2)
		checkForMembership(name, last)
		temp = []
		Dtime = datetime.datetime.now()# Issue Date
		Rtime = datetime.datetime.now() + datetime.timedelta(days=7)# Due Date
		data = [titleName, Dtime.strftime("%d/%m/%Y"), Rtime.strftime("%d/%m/%Y"), name, "Pending"]
		temp.append(data)
		readWriteFile.writeFile('BookAvailability.txt', temp, 'a')
		dashboard.updateFileDashboard(titleName, "minus") # Decrease the Qty from Available Stack
		print("Book Issued Successfully.\nThank You.")
		exit()
	else:
		dashboard.display()





def checkBook(response):
	rows=readWriteFile.readFile('Materials.txt')
	Dtime = datetime.datetime.now()
	flag = 0
	for row in rows:
		if row[0] == response:
			flag = 1
			if row[5] != '0':
				print(response,"is Available. Quantity: "+row[5]+"/"+row[6])
				borrowBook(response)

	if flag == 0:
		print("No such book available. Please enter the name CORRECTLY")
		readWriteFile.loading('Terminating ......', 2)
		print("Terminated")
		exit()
	else:
		rows=readWriteFile.readFile('BookAvailability.txt')
		temp = []
		for row in rows:
			#check for min number of days for book availability
			if row[0] == response and datetime.datetime.strptime(row[2], "%d/%m/%Y") > Dtime:
				temp.append(row[2])

		if len(temp) == 0:
			print("\nSorry For the inconvenience cause. The book has not returned from borrower yet.")
			print("\nPlease check again tomorrow.")
			exit()
		else:
			dte=min(temp)
			print(response,"book is currently Unavailable.\nProvisional availability of this book will be on",dte)
			print("\nThank You, Have a nice Day.")
			exit()
