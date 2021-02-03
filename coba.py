start = False
while True:
    command = input("> ").lower()
    if command == "help":
        print ('''
start - to start the car
stop - to stop the car
quit - to exit ''') 
    elif command == "start":
        if start :
            print(" Hey ! car already start")
        else :
            start = True
            print ("car started ... Ready to go !")
    elif command == "stop":
        if not start:
            print ("Hey car already stopped")
        else :
            print ("car Stopped")
            start = False
    elif command == "quit":
        break
    else:
        print( "I don't Understand that")
     
