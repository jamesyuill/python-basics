# start = to start the car
# stop - to stop the car
# quite - to exit

command = ""
isCarStarted = False


while True:
    command = input('> ').lower()
    if command == 'start':
        if isCarStarted:
            print('Car is already started')
        else:
            isCarStarted = True
            print('Car started...')
    elif command == 'stop':
        if not isCarStarted:
            print('Car is already stopped')
        else:
            isCarStarted = False
            print("car stopped.")
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit""")
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand")