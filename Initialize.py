
from Socket import sendMessage
def joinRoom(s):
	readbuffer = "" #string that contains info communicated to and from the socket
	Loading = True
	while Loading:
		readbuffer = readbuffer + (s.recv(1024).decode('utf-8'))
		temp = readbuffer.split("\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	sendMessage(s, "Successfully joined chat".encode('utf-8'))
	
def loadingComplete(line): #to escape from the infinite loop
	if("End of /NAMES list" in line): #twitch sends this line back once it has finished loading
		return False
	else:
		return True