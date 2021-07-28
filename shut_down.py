import random
a = "dfdfdf", "fdfdfdfdf", "dfdfdfdf"
print(random.choice(a))




while True:
    print('''1. roll the die
2. exit''')
    user = int(input("what you want to do:\n"))
    if user==1:
        number = random.randint(1,6)
        print(number)
    else:
        break