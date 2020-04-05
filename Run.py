from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
import pickle

s = openSocket()
joinRoom(s)
readbuffer = ""

class Database:
    def __init__(self,qns,ans): #function to initialise values
        self.qns=qns
        self.ans=ans
    def get_qns(self): #function to return the qns
        return self.qns
    def get_ans(self): #function to return the ans
        return self.ans
    def set_qns(self,qns): #function to set the qns
        self.qns=qns
    def give_ans(self): #function to take answer from Streamer when not known
        self.ans=input("ENTER THE ANSWER: ")
        
o1=Database("hello","hello")

while True:
    readbuffer = readbuffer + (s.recv(1024).decode('utf-8'))
    temp = readbuffer.split("\n")
    readbuffer = temp.pop()
    
    for line in temp:
        print(line)
        if "PING" in line: #to tell twitch that we are not third party. we need to return pong
            s.send(line.replace("PING", "PONG").encode('utf-8'))
            break
        user = getUser(line)
        message = getMessage(line)
        print (user + " typed :" + message) # to see in cmd prompt
        
        f=open("qns.dat","rb") #binary file in read mode
        flag=-1
        try:
            while True:
                o=pickle.load(f)
                #checking if a reply to qns exists
                if o.get_qns() in message:
                    a=o.get_ans()
                    sendMessage(s,a.encode('utf-8'))
                    flag=0
                    break
        except EOFError:  
            f.close()
        f=open("qns.dat","ab+")    
        if flag==-1:
                #setting reply to the unknown qns
                sendMessage(s,"I dont know what to reply to this ! I will get back to you".encode('utf-8'))
                o=Database("","")
                o.set_qns(message)
                o.give_ans()
                pickle.dump(o,f)
                f.close()
            