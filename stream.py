class Stream:
	def __init__(self, name, test = True):
		self.name = name
		self.test = test
		
	def output(self,data):
		if test:
			print "STREAM(",self.name,"):",data
			
class MessageStream:
	def __init__(self):
		self.stream = Stream("MESSAGE")
	
	def output(self,data):
		self.stream.output(data)
		
class UnitStream:
	def __init__(self):
		self.stream = Stream("UNITS")
	
	def output(self,data):
		self.stream.output(data)
		
class TownStream:
	def __init__(self):
		self.stream = Stream("TOWNS")
	
	def output(self,data):
		self.stream.output(data)
		
class SettingsStream:
	def __init__(self):
		self.stream = Stream("SETTINGS")
	
	def output(self,data):
		self.stream.output(data)
		
default = SettingsStream

def printData(data):
	default.output(data)