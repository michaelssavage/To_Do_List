class Task:

	def __init__(self, job, date, time, duration, people):
		self.job = job
		self.date = date
		self.time = time
		self.duration = duration
		self.people = people

	def __str__(self):
		return "{}, {}, {}, {}, {}".format(self.job,
										   self.date,
										   self.time,
										   self.duration,
										   self.people)
