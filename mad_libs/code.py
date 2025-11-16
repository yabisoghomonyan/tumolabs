import random
x=random.randint(1,3)
print(f"You choose {x} story")
print("Enter the inputs to make you story ")
print("\n")
while True:
    if x==1:
        try:
            Number = input("Enter the number: ")
            Time = input("Enter the measure of time: ")
            Transportation = input("Enter the mode of transportation: ")
            Adjective1 = input("Enter the adjective: ")
            Adjective2 = input("Enter another adjective: ")
            Noun1 = input("Enter a noun: ")
            Color = input("Enter a color: ")
            Body1 = input("Enter a body part: ")
            Verb1 = input("Enter a verb: ")
            Number2 = input("Enter another number: ")
            Noun2 = input("Enter another noun: ")
            Noun3 = input("Enter a noun: ")
            Body2 = input("Enter another body part: ")
            Verb2 = input("Enter another verb: ")
            Noun4 = input("Enter another noun: ")
            Adjective3 = input("Enter another adjective: ")
            Silly_Word = input("Enter a silly word: ")
            Noun5 = input("Enter one last noun: ")
            inputs = [Number, Time, Transportation, Adjective1, Adjective2, Noun1, Color,
                      Body1, Verb1, Number2, Noun2, Noun3, Body2, Verb2, Noun4,
                      Adjective3, Silly_Word, Noun5]
            if any(value.strip() == "" for value in inputs):
                raise ValueError(" All parts must be filled!")
            for value in inputs:
                if  len(value.split()) > 1:
                    raise ValueError(" Only 1 word allowed!")
            print("\n")
            print(f''' It was about {Number} {Time} ago when I arrived at the hospital in a {Transportation}. The hospital is a/an {Adjective1} place, there are a lot of {Adjective2} {Noun1} here."
                         There are nurses here who have {Color} {Body1}. If someone wants to come into my room I told them that they have to {Verb1} first. I’ve decorated my room with {Number2} {Noun2}."
                         Today I talked to a doctor and they were wearing a {Noun3} on their {Body2}. I heard that all doctors {Verb2} {Noun4} every day for breakfast."
                         The most {Adjective3} thing about being in the hospital is the {Silly_Word} {Noun5} ! ''')
            break
        except ValueError as e:
            print(f"Invalid input: all parts must be filled.{e}")
    elif x==2:
        try:
            Proper_Noun = input("Enter the proper noun (person's name): ")
            Noun1 = input("Enter a noun: ")
            Feeling1 = input("Enter a feeling: ")
            Verb1 = input("Enter a verb: ")
            Feeling2 = input("Enter another feeling: ")
            Animal = input("Enter an animal: ")
            Verb2 = input("Enter another verb: ")
            Color1 = input("Enter a color: ")
            Verb3 = input("Enter a verb ending in -ing: ")
            Adverb = input("Enter an adverb ending in -ly: ")
            Number1 = input("Enter a number: ")
            Time = input("Enter a measure of time: ")
            Color2 = input("Enter another color: ")
            Animal2 = input("Enter another animal: ")
            Number3 = input("Enter another number: ")
            Silly_Word = input("Enter a silly word: ")
            Noun2 = input("Enter another noun: ")
            inputs = [Proper_Noun, Noun1, Feeling1,Verb1,Feeling2,Animal,Verb2,
                      Color1, Verb3, Adverb, Number1, Time, Color2, Animal2,
                      Number3, Silly_Word, Noun2]
            if any(value.strip() == "" for value in inputs):
                raise ValueError(" All parts must be filled!")
            for value in inputs:
                if  len(value.split()) > 1:
                    raise ValueError(" Only 1 word allowed!")
            print("\n")
            print(f''' This weekend I am going camping with {Proper_Noun }. I packed my lantern, sleeping bag, and {Noun1}. "
                        I am so {Feeling1} to {Verb1} in a tent. I am {Feeling2} we might see a(n) {Animal}, I hear they’re kind of dangerous."
                        While we’re camping, we are going to hike, fish, and {Verb2}. I have heard that the {Color1} lake is great for {Verb3}."
                        Then we will {Adverb} hike through the forest for {Number1} {Time}. If I see a {Color2} {Animal2} while hiking, I am going to bring it home as a pet!"
                        At night we will tell {Number3} {Silly_Word} stories and roast {Noun2} around the campfire!! ''')
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
    else:
        try:
            Proper_Noun = input("Enter the proper noun (person's name): ")
            Adjective1=input("Enter the adjective: ")
            Color=input("Enter the color: ")
            Animal=input("Enter the animal: ")
            Place=input("Enter the place: ")
            Adjective2=input("Enter the adjective: ")
            Magical_Creature1=input("Enter the magical creature(Plural): ")
            Adjective3=input("Enter the adjective: ")
            Magical_Creature2=input("Enter the magical creature(Plural): ")
            House_Room=input("Enter the house room: ")
            Noun1=input("Enter the noun: ")
            Noun2=input("Enter the noun(Plural): ")
            Adjective4=input("Enter the adjective: ")
            Noun3=input("Enter the noun: ")
            Time=input("Enter the measure of time: ")
            Noun4=input("Enter the noun(Plural): ")
            Number=input("Enter the number: ")
            Verb1=input("Enter the verb+ing: ")
            Adjective5=input("Enter the adjective: ")
            Noun5=input("Enter the noun: ")
            print("\n")
            inputs = [Proper_Noun, Noun1, Adjective1,Verb1,Magical_Creature1,Animal,Adjective3,Magical_Creature2,
                      Color, House_Room, Adjective4, Noun3, Time,Noun4, Adjective5,
                      Number, Noun5]
            if any(value.strip() == "" for value in inputs):
                raise ValueError(" All parts must be filled!")
            for value in inputs:
                if  len(value.split()) > 1:
                    raise ValueError(" Only 1 word allowed!")
            print("\n")
            print(f''' Dear {Proper_Noun}, I am writing to you from a {Adjective1} castle in an enchanted forest."
                         I found myself here one day after going for a ride on a {Color} {Animal} in {Place}. "
                         There are {Adjective2} {Magical_Creature1} and {Adjective3} {Magical_Creature2} here!"
                         In the {House_Room} there is a pool full of {Noun1}. I fall asleep each night on a {Noun2} of {Noun3} and dream of {Adjective4} {Noun4}. "
                         It feels as though I have lived here for {Number} {Time}."
                         I hope one day you can visit, although the only way to get here now is {Verb1} on a {Adjective5} {Noun5}!!''')
            break
        except ValueError as e:
            print(f"Invalid input: all parts must be filled.{e}")
