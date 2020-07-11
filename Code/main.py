import dashboard 
import returnBook
import readWriteFile


def chooseMenu(option):
	if option == 1:
		dashboard.display()
	elif option == 2:
		dashboard.borrowSearch()
	elif option == 3:
		returnBook.bookReturn()
	elif option == 4:
		createNew()
	elif option == 5:
		exit()
	else:
		print("You have entered the wrong value.\nPlease select the CORRECT option from Menu")
		print("1. Display Dashboard\t2. Borrow Book\t3. Return Book\t4. New Membership\t5. Exit")
		option = int(input())
		chooseMenu(option)



def createNew():
	print("\n************ New Membership ************")
	print("\nDetails :\nEnter your First Name :")
	fName = input()
	print("\nEnter your Last Name :")
	lName = input()
	print("\nEnter your Mobile number :")
	mNum = input()
	temp = []
	data = [fName, lName, mNum, "YES"]
	temp.append(data)
	readWriteFile.writeFile('NewMember.txt', temp, 'a')
	print("\nCongratulations You Have Successfully Created New Membership")
	print("\nRedirecting to Display Dashboard")
	readWriteFile.loading('redirecting ..........', 3)
	dashboard.display()



def main():
	print("\nWelcome to Central Library - Panaji, Goa")
	print("Please select one option from Menu")
	print("1. Display Dashboard\t2. Borrow Book\t3. Return Book\t4. Membership Plan\t5. Exit")
	option = int(input())
	chooseMenu(option) 




if __name__ == '__main__':
	main()
