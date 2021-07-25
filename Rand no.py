import random
n = random.randint(1, 20)
for i in range(0, 3):
    user = int(input("Guess the number: "))
    if user == n:
        print("Hurray!")
        print(f"you guessed the number right it's {n}")
        break
    if user != n:
        print(f"Your guess is incorrect, the number is {n}")