import os

cart = []
isQuit = False

def add():
    os.system('cls')
    name = input("Please, type name of the product which you want to add into your shopping cart: ")
    cart.append(name)
    print(f"{name} has been added into your shopping cart")
    input('Press Enter to return to the command menu...')

def remove():
    os.system('cls')
    name = input("Please, type name of the product which you want to remove from your shopping cart: ") 
    try:   
        cart.remove(name)
        print(f"{name} has been removed from your shopping cart")
    except:
        print("For some reason we can't remove this good. Probably it's not in your shopping cart")
    input('Press Enter to return to the command menu...')

def clear():
    os.system('cls')
    print("All goods have been removed from your shopping cart")
    input('Press Enter to return to the command menu...')
    return []

def show():
    os.system('cls')
    print(f"In your shopping cart you have:\n{cart}")
    input('Press Enter to return to the command menu...')

def quit():
    os.system('cls')
    print("Have a nice day!")
    return True

print("Welcome to our shop!")
while not isQuit:
    os.system('cls')
    print("To add a good into your shopping cart type 'add' command and follow instructions")
    print("To remove a good from your shopping cart type 'remove' command and follow instructions")
    print("To remove all goods from your shopping card type 'clear' command")
    print("To show all goods in your shopping cart type 'show' command")
    print("To quit type 'quit' command")
    inpt = input("Please type a command: ")
    if inpt.lower() == 'add':
        add()
    elif inpt.lower() == 'remove':
        remove()
    elif inpt.lower() == 'clear':
        cart = clear()
    elif inpt.lower() == 'show':
        show()
    elif inpt.lower() == 'quit':
        isQuit = quit()
    else:
        print("Unknown command. Please, try again.")
