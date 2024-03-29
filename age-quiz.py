#This code is for an age quiz
#The user inouts there age and the test output is dependent on their age range
#added elements to ensure inappropriate inputs will not be accepted
#Check to ensure the input in numeric. if not then print invalid inout
#also print invalid input for negative values

age = (input("What is your age? Inout need to be in years not months"))
numeric = age.isnumeric()

#numeric input check
if numeric == True:
    age_int  = int(age)
    if age_int == 100:
        print("congrats on your letter from the king")
    elif age_int > 100:
        print("Sorry you are dead.")
    elif age_int >= 65:
        print("Enjoy your retirment!")
    elif age_int >= 40:
        print("You're over the hill")
    elif (age_int < 13): 
        print("You qualify for kiddie discount.")
    elif age_int == 21:
        print("Congrats on your 21st!")
#positive input check
    elif age_int < 0:
        print("This is an invalid age!")
    else:
        print("Age is but a number.")
else: 
    print ("This is an invalid input")
