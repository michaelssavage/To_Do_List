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

	print("Show all jobs: ")
	q.showAll()

	print("remove first job: ")
	q.dequeue()

	print("add job: ")
	concert = Event("U2 gig", "Tomorrow", "8pm", "London")
	print(concert)
	q.enqueue(concert)

	#
	print("first job: ")
	q.todo()

	print("Show all jobs: ")
	q.showAll()

	q.dequeue()
	q.dequeue()
	q.dequeue()

	print("Show all jobs: ")
	q.showAll()

if __name__ == '__main__':
	main()