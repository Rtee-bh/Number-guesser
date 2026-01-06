# RANDOM NUMBER GUESSING GAME
import random
secret_number= random.randint(0, 50)
b="hey!!! welcome to the number guessing game :"
print(b.center(80,"*"))
print("Try your luck and guess the number.\n The number are between 0 to 50.")
a= -1
attempts= 0
a= int(input("Hey anonymous, plz enter the number you guessed:"))
while secret_number != a:
 if(a>secret_number):
    print("oops! please guess the smaller number.")
    a= int(input("enter your new guess:"))
    attempts+= 1
 elif(a<secret_number):
    print("oops! please guess the larger number.")
    a= int(input("enter your new guess:"))
    attempts+= 1
else:
    print("Congratulations! you guessed the correct number in", attempts, "attempts.\nThankyou for playing the game.")
    
 
