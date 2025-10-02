import random
def trow():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    goal=dice1+dice2
    return dice1,dice2,goal
def result():
    dice_1,dice_2,goal=trow()
    print(f"The sum of dice is {dice_1} + {dice_2} = {goal}")
    if goal in (7, 11):
        print("You won")
    elif goal in (2,3,12):
        print("You lose")
    else:
        print(f"Now your goal number is {goal}")
        while True:
            dice_1,dice_2,goal1=trow()
            print(f"The sum of dice is {dice_1} + {dice_2} = {goal}")
            if goal1==7:
                print("You lose")
                break
            elif goal1==goal:
                print("You won")
                break
result()
