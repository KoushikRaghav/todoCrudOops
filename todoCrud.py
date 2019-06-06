todoItems = []

class todo:
	def __init__(self,goal):
		self.goal = goal

	def setGoal(self,todoGoal):
		self.goal = todoGoal

	def getGoal(self):
		return self.goal

def deleteToDo():
	sNum = int(input("\nEnter the serial number: "))
	del todoItems[sNum]
	print "\nContact deleted successfully"

def updateToDo():
	sNum = int(input("\nEnter the serial number: "))
	itemm = todoItems[sNum]
	print todoItems
	todoGoal = raw_input("\nEnter replacement goal: ")
	itemm.setGoal(todoGoal)
	print "\nGoal is updated as {}".format(todoGoal)

def readToDo():
	for idd,item in enumerate(todoItems):
		print("{}.{}".format(idd,item.getGoal()))

def createToDo():
	global todoItems
	goal = raw_input("\nEnter the todo: ")
	newgoal = todo(goal)
	todoItems.append(newgoal)

def getCrud():
	option = int(input("\nEnter option to manage your todo list:\n\n1. Create\n2. Read\n3. Update\n4. Delete\n5. Exit\n\n"))
	return option	

def main():
	print "<--- TODO LIST --->"
	while 1:
		option = getCrud()
		if option == 1:
			createToDo()
		elif option == 2:
			readToDo()
		elif option == 3:
			readToDo()
			updateToDo()
		elif option == 4:
			readToDo()
			deleteToDo()
		elif option >=5:
			print "\nBYE"
			exit()

if __name__ == '__main__':						
	main()