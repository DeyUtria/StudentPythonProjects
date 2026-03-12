from random import randint

results = []
count = 0
user_option = input("Please choose your option between heads or tails: ")

while count < 1:
    value = randint(0, 1)
    if user_option == "Heads" and value == 0:
        results.append(value)
        count += 1
        print("The result was " + str(value) + " so you won!")
    elif user_option == "Tails" and value == 1:
        results.append(value)
        count += 1
        print("The result was " + str(value) + " so you won!")
    else:
        results.append(value)
        count += 1
        print("The result was " + str(value) + " so you lost :(")
    break