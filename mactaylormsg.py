from line import sys, LineClient, LineGroup, LineContact

try:
    client = LineClient(authToken="04Unk=")
    friend = client.contacts[2]
except:
    print "Login Failed"

while True:
    friend.sendMessage("Hello world");
    break