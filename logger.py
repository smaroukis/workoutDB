from datetime import datetime as dt

# TODO add workout class so we can pass it to workout.log
class Logger:

		def __init__(self, filepath):
			with open(filepath, 'r') as file:
				self.filepath=filepath
				self.logger=(file.read())
				self.today=str(dt.today().date())

		def log(self, id, type, duration, intensity, description, tag):
				self.logcache='{}: {}, {}, {}, {}, {}, {}'.format(self.today, id, type, duration, intensity, description, tag)
				# actually, why do you need all this information in the log? A: you don't: find a better descriptive short id

		def clear(self):
				self.logcache=""

		def commit(self):
				with open(self.filepath, 'a') as file:
						file.write(self.logcache + "\n")

#logger = Logger("log.txt")
#logger.log(1, 'run', 40, 'high', 'description test', 'tag test')
#logger.commit()
