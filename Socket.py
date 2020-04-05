import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():
	#the following is the protocol followed by IRC
	s = socket.socket() #declares s to be a socket
	s.connect((HOST, PORT)) #connects to the host server
	s.send(("PASS " + PASS + "\r\n").encode('utf-8')) #sends the authorisation key received from twitch
	s.send(("NICK " + IDENT + "\r\n").encode('utf-8'))
	s.send(("JOIN #" + CHANNEL + "\r\n").encode('utf-8'))#joins the chat room channel
	return s
	
def sendMessage(s, message): #function for bot to send message
	messageTemp = ("PRIVMSG #" + CHANNEL + " :" + message.decode('utf-8'))
	s.send((messageTemp + "\r\n").encode('utf-8'))
	print("Sent: " + messageTemp) #to check what is being sent to twitch in command prompt
