isRunning = True
carIsStarted = False
print("Type 'help' to see the list of available commands.")
inputContainer = ''
while isRunning:   
    inpt = input('> ')    
    if inpt == 'help':       
        print("Type 'start' to start the car.")
        print("Type 'stop' to start the car.")
        print("Type 'quit' to quit program.")
    elif inpt == 'start' and not carIsStarted:
        carIsStarted = True
        print('The car is started... Ready to go!')       
    elif inpt == 'start' and carIsStarted:
        print('The car is already started.')
    elif inpt == 'stop' and carIsStarted:
        carIsStarted = False
        print('The car is stopped.')
    elif inpt == 'stop' and not carIsStarted:
        print('The car is already stopped.')
    elif inpt == 'quit':
        isRunning = False
    else:
        print("Incorrect input. Please type 'help' to see the list of available commands.")
        
        
