from task import Task
from queue import Queue
from event import Event
import sys
import re

def main():
	q = Queue()

	q.commands()
	
	job = input("Enter: ")
	while job != 'q':

		#get rid of any unwanted spaces
		job = job.lower().strip()

		if job == 'job':
			#print the first job
			print(q.todo())

		elif job == 'all':
			#print out all the jobs to be done
			q.showAll()

		elif job == 'r':
			#remove the job with a confirmation
			done = input("Do you want to remove first job? (y/n): ")
			if done == "y":
				q.dequeue()

		elif job == 'add e':
			#go to add event
			addEvent(q)
			print("Event added.")

		elif job == 'add t':
			#go to add task
			addTask(q)
			print("Task added.")

		elif job == 'help':
			q.commands()

		else:	
			print("That is not a command.")

		#repeat until quit
		job = input("Enter: ")
	print("Bye!")

def addTask(q):

	#Task has a date, start time, duration, and list of assigned people.
	newTask = Task(input("Task Name: "), 
		input("Date: "), 
		input("Start Time: "),
		input("Duration: "), 
		re.findall(r"[\w']+",input("People assigned to task: ")))
	q.enqueue(newTask)

def addEvent(q):

	#Event has a date, start time, and location
	newEvent = Event(input("Event Name: "), 
		input("Date: "), 
		input("Start Time: "),
		input("location: "))
	q.enqueue(newEvent)


if __name__ == '__main__':
	main()