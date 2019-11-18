from task import Task
from queue import Queue
from event import Event
import sys
import re

def main():
	q = Queue()
	q.enqueue(Task("Football","25/12/2024","21:00","4hrs",["Pat"]))
	q.enqueue(Task("Buy milk","12/1/2039","11:00","4.30hrs",["John","Mary","Ben"]))
	q.enqueue(Event("New Years","1/1/2020","12:00","Dublin"))

	print("1. Show all jobs: ")
	#there should be 3 jobs.
	q.showAll()

	print("2. Remove first job.")
	#remove football
	q.dequeue()

	print("3. Add Event: ")
	#add event
	concert = Event("U2 gig", "Tomorrow", "8pm", "London")
	print(concert)
	q.enqueue(concert)

	#
	print("4. First job: ")
	#should be buy milk
	print(q.todo())

	print("5. Show all jobs: ")
	#should milk, new years, and u2
	q.showAll()

	print("6. Remove first job.")
	print("7. Remove first job.")
	print("8. Remove first job.")
	q.dequeue()
	q.dequeue()
	q.dequeue()

	print("9. Show all jobs: ")
	#should be empty.
	q.showAll()

if __name__ == '__main__':
	main()
