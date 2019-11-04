import random
print "--- Welcome to 'Guess the Number' Game V.0.3 ---"

user_name=""
password=""

def main_menu():
    print "1. Login \n2. Sign Up (Limited to 1 user) \n3. Description"
    choice = input("->")
    while choice<0 or choice>3:
        choice = input("->")
    if choice == 1:
        log_in()
    elif choice == 2:
        if user_name != "" or password != "":
            print "You have already signed up, you can't sign up more than 1 user!"
            print "Going back to main menu..."
            main_menu()
        else:
            sign_up()
    elif choice == 3:
        print "This project is 'ENGR 101 - Introduction to Programming' course's mini project 01. \nThe project is a game played by one player by sign up and login system. \nThe player should assume the randomly generated number and accordingly he/she will earn or lose points."
        print "Going back to main menu..."
        main_menu()

def log_in():
    while user_name == "" or password == "":
        print "Warning! There is no users :( Please sign up first\nGoing back to main menu..."
        main_menu()
    enter_user_name = raw_input("User Name: ")
    enter_password = raw_input("Password: ")
    while enter_user_name != user_name or enter_password != password:
        print "User Name or Password is wrong! Please try again."
        enter_user_name = raw_input("User Name: ")
        enter_password = raw_input("Password: ")
    game()

def sign_up():
    global user_name
    global password
    define_user_name=raw_input("Please define a user name:")
    define_password=raw_input("Please define a password:")
    user_name=define_user_name
    password=define_password
    main_menu()

def game():
 point = 100
 while True:
     print "Let's start with a new number"
     print "Your Point:{}".format(point)
     machine = random.randint(1, 50)
     print machine
     guess = input("Guess The Number:")
     print "Python:",machine,"Guess:",guess
     if guess == machine:
        point = point + 25
        print "Your Point:{}".format(point)
        print"Congratulations, that's right. You got +25 Points"

     elif guess >= (machine * 2):
        point = point - 10
        print "Your Point:{}".format(point)
        print "The number you guess is too high. You lose 10 Points"

        print "You still have a chance. Try Again!"

     elif (machine + 1) <= guess <= (machine*2 -1):
        point = point - 5
        print "Your Point:{}".format(point)
        print"The number you guess is too high. You lose 5 Points"
        print "You still have a chance. Try Again!"

     elif guess <= (machine / 2):
        point = point - 10
        print "Your Point:{}".format(point)
        print "The number you guess is too low. You lose 10 Points"
        print "You still have a chance. Try Again! "

     elif (machine - 10) <= guess <= (machine - 1):
        point = point - 5
        print "Your Point:{}".format(point)
        print "The number you guess is too low. You lose 5 Points"
        print "You still have a chance. Try Again! "

     if point == 0:
       print " > Your Point is ZERO >"
       print "--------------------------------"
       print "----- < Game Over > -----"
       print "--------------------------------"
       main_menu()

main_menu()
sign_up()
game()