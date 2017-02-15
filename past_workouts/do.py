from datetime import datetime as dt

today = dt.today().date()

class FinishedWorkout:

		def __init__(self, filepath):
			with open(filepath, 'r') as file:
				self.filepath=filepath
				self.logger=(file.read())

		def log(self, workout):
				self.logger=self.logger + str(today) + ": " + workout

		def clear(self):
				self.logger=""

		def commit(self):
				with open(self.filepath, 'w') as file:
						file.write(self.logger)

fin_wo = FinishedWorkout("past_workouts/done.txt")
fin_wo.log("added")
print(fin_wo.logger)
fin_wo.commit()
