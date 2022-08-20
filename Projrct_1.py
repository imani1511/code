import random
real = random.randint(1, 100)
# print (real)
point = 100

while True:
    num = int(input("Enter the your guess(1-100)\n"))
    if num < real:
        point = point-1
        count = count+1
        print("\nYour guess is smaller than the number\n")

    elif num > real:
        print("\nYour guess is higher\n")
        point = point-1
        count = count+1

    else:
        print("\nYour guess was right")
        break
print(f"Your point is {point}")
