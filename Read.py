def getUser(line): #function that returns which user entered the line to the streamer
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user
def getMessage(line): #function that returns the message entered by the user
	separate = line.split(":", 2)
	message = separate[2]
	return message