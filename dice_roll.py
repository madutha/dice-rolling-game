import random
play = True

while True:
    choice = input("roll the dice (y/n): ").lower()
    if choice == 'y':
        die1 = random.randint(1,6)
        print(f"{die1}")
    elif choice == 'n':
        print("thank you for playing!")
    else:
        print("invalid character!")

