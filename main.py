import stream
import saving

def setUpSettings():
	stream.default = stream.SettingsStream
	stream.printData("Settings")
	stream.printData("Enter the player name: ")
	
	
