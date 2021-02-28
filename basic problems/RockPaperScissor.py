import random
print("Welcome to Rock Paper and Scissor Game :)")

while True:
    print('Enter your Choice from "R" "P" or "S"')
    user = input().upper()
    if user not in ["R", "P", "S"]:
        print("Invalid Input")
    else:
        comp = random.choice(["R", "P", "S"])
        print(f"My choice is: {comp}")
        choice = [comp == "R" and user == "P",
                  comp == "P" and user == "S",
                  comp == "S" and user == "R"]
        if any(choice):
            print("Cool,You Win.")
        elif comp == user:
            print("Draw.")
        else:
            print("I win, You lose.")

    print("\nContinue? Y or N")
    ans = input()
    if ans.upper() == "N":
        print("See You Again..")
        break
