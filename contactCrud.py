allContacts = []

class Contact:
	def __init__(self,name,contactNum):
		self.Uname = name
		self.contactNumber = contactNum
	
	def setNum(self,mobileNumber):
		self.contactNumber = mobileNumber

	def getName(self):
		return self.Uname

	def getNum(self):
		return self.contactNumber	

def deleteContact():
	sNum = int(input("\nEnter the serial number: "))
	del allContacts[sNum]
	print "\nContact deleted successfully"

def checkList():
	if len(allContacts)== 0:
		return 0
	else:
		return 1
   
def updateContact():
	sNum = int(input("\nEnter the serial number: "))
	contact = allContacts[sNum]
	print allContacts
	mobileNumber = input("\nEnter replacement number: ")
	if checkForDigits(mobileNumber) == 1:
		contact.setNum(mobileNumber)
		print "\nThe contact number of {} is updated to {}".format(contact.getName(),mobileNumber)
	else:
		print "Enter a 10 digit number to update"
		updateContact()
	
def readContact():
	if checkList() == 1:
		for contactList in allContacts:
			print "{}. {} --> {}".format(allContacts.index(contactList), contactList.getName(),contactList.getNum()) 		
		return 1
	else:
		print "\nCreate a Contact first"
		return 0	

def checkForDigits(contactNum):
	count = len(str(contactNum))
	if count == 10:
		return 1
	else:
		return 0

def createContact():
	global allContacts
	name = raw_input("\nEnter Contact Name: ")
	contactNum = raw_input("\nEnter Contact Number: ")
	if checkForDigits(contactNum) == 1:
		newContact = Contact(name,contactNum)
		allContacts.append(newContact)
		print "\n{} is added in the contact list".format(newContact.getName())
	else:
	 	print "\nEnter a 10 digit number to create"
	 	createContact()
		
def getCrud():	
	option = int(input("\nEnter option to manage your contact list:\n\n1. Create Contact\n2. Read all contacts\n3. Update Contact List\n4. Delete Contact\n5. Exit\n\n"))
	return option	

def main():
	print "<--- CONTACT MANAGEMENT --->"
	while 1:
		option = getCrud()
		if option == 1:
			createContact()
		elif option == 2:
			read = readContact()
		elif option == 3:
			read = readContact()
			if read == 1:
				updateContact()
			else:
				createContact()
		elif option == 4:
			read = readContact()
			if read == 1:
				deleteContact()
			else:
				createContact()			
		elif option >= 5:
			print "BYE"
			exit()
	   
if __name__ == '__main__':						
	main()