class Event:

	def __init__(self, job, date, time, location):
		self.job = job
		self.date = date
		self.time = time
		self.location = location

	def __str__(self):
		return "{}, {}, {}, {}".format(self.job,
									   self.date,
									   self.time,
									   self.location)
