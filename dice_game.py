import random
def trow():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    return dice1,dice2
def result():
    dice_1,dice_2=trow()
    goal=dice_1+dice_2
    if goal==11 or goal==7:
        print(f"The sum of dice is {dice_1} + {dice_2} = {goal}")
        print("You won")
    elif goal==12 or goal==2 or goal==3:
        print(f"The sum of dice is {dice_1} + {dice_2} = {goal}")
        print("You lose")
    else:
        print(f"The sum of dice is {dice_1} + {dice_2} = {goal}")
        print(f"Now your goal number is {goal}")
        while True:
            dice_1,dice_2=trow()
            goal1=dice_1+dice_2
            if goal1==7:
                print(f"The sum of dice is {dice_1} + {dice_2} = 7")
                print("You lose")
                break
            elif goal1==goal:
                print(f"The sum of dice is {dice_1} + {dice_2} = {goal}")
                print(" You won")
                break
            else:
                print(f"The sum of dice is {dice_1} + {dice_2} = {goal}")
result()