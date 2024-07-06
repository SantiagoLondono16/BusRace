import random
import os
import time

def console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def advance(bus):
    if random.random() >= 0.5:
        for i in range (4):
            bus[i] = '  ' + bus[i]
    else:
        for i in range (4):
            bus[i] = ' ' + bus[i]
    return bus

columns = os.get_terminal_size().columns
bar = '-' * columns

redBus = [" _________________",
          "|               |_|__",
          "|       Red          |",
          "|---O------------O---|"]

blueBus = [" _________________",
          "|               |_|__",
          "|       Blue         |",
          "|---O------------O---|"]

winner = input('Select a winner (Red/Blue):')
for i in range(5):
    console()
    print(5-i)
    time.sleep(0.5)
    
    
flag = True
while flag:
    console()
    print (bar)

    for i in redBus:
        print(i)

    print (bar)

    for i in blueBus:
        print(i)

    print(bar)

    if len(redBus[2]) >= columns-1 or len(blueBus[2]) >= columns-1:
        if len(redBus[2]) > len(blueBus[2]):
            print("Red Win")
            if winner == 'Red':
                print('You got it right!')
            else:
                print("You didn't get it right!")
        elif len(redBus[2]) < len(blueBus[2]):
            print("Blue Win")
            if winner == 'Blue':
                print('You got it right!')
            else:
                print("You didn't get it right!")
        else:
            print("Draw")
        flag = False
    
    redBus = advance(redBus)
    blueBus = advance(blueBus)
    time.sleep(0.1)