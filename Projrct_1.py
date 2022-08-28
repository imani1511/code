import random
real = random.randint(1, 100)
# print(real)
point = 10
chance = 10
flag = True
while flag:
    while chance > 0:
        num = int(input("Enter the your guess(1-100)\n"))
        if num < real:
            point = point-1
            chance = chance-1
            print("\nYour guess is smaller than the number\n")
        elif num > real:
            print("\nYour guess is higher\n")
            point = point-1
            chance = chance-1
        if num < 0:
            print("Please enter a valid input")
            num = int(input("Enter the your guess(1-100)\n"))
            point = point-1
            chance = chance-1
            break
        if num == real:
            print("\nYour guess was right")
            print(f"Your point is {point}")
            flag = False
            break
        elif chance == 0:
            print("You are out of chances")
            print("Better luck next time")
            print(f"Your point is {point}")
            flag = False
            break
        break
