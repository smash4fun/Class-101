import random 


while True:
     

    response = input('Do you want to roll the dice? Type y for yes or n for no     ')


    if response == "y":
        number = random.randint(1, 6)

        if number == 1:
             print(number)
             print("*")

        if number == 2:
             print(number)
             print("*  *")

        if number == 3:
             print(number)
             print("* * *")

        if number == 4:
             print(number)
             print("*  *")
             print("*  *")

        if number == 5:
             print(number)
             print("*   *")
             print("  *  ")
             print("*   *")

        if number == 6:
             print(number)
             print("*   *")
             print("*   *")
             print("*   *")

        continue
    else:
        print("Maybe next time")
        break