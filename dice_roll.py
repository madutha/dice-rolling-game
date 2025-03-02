import random

i=1
choice = input("roll the dice (y/n): ").lower()
roll = int(input("How many times do you want to roll?\n"))

while(i<=roll):
    if choice == 'y':
        die1 = random.randint(1,6)
        print(f"{die1}")
    elif choice == 'n':
        print("thank you for playing!")
    else:
        print("invalid character!")
    i += 1
