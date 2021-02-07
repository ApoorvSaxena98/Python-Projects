import random
min = 1
max = 6
roll_again = "yes"

while roll_again == "yes" or roll_again == "y" or roll_again == "Y" or roll_again == "YES" or roll_again == "Yes":
    print("The Values are :")

    # generating and printing 1st random integer from 1 to 6
    print(random.randint(min, max))

    # asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input("Roll the Dices Again? (Yes/No)")



#import random
#s = random.randint(0, 10)
#print("Random number is: ", s)
