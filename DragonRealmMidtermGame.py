# Dragon Realm
# A game by Amanda Huynh
# December 22, 2017

# import stuff
import random
import time

# Global Variables
score = 0

# Show Introduction
def show_intro():
    print('''You've lost your map and there seems to be
no trace of the merchant's caravan you stowed away on.
In one cave, the dragon is friendly
and will share his treasure with you. The other dragon is
greedy and hungry, and will eat you on site.''')
    print()


def choose_cave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into? (1 or 2)")
        cave = input()
    return cave

def check_cave(cave_chosen):
    global score
    print("You approach the mouth of the cave slowly...")
    time.sleep(2)
    print("You catch a whif of strong-smelling dung and rotten flesh ...")
    time.sleep(4)
    print("You walk deeper into the cave and see MAGNIFICENT piles of TREASUREEEE!!")
    time.sleep(4)
    print('''You jump around and scream for joy!
You grab handfuls of stolen treasure and stuff them into your pockets and bag.''')
    time.sleep(6)
    print()
    print("Suddenly, you hear loud thumps at the back of the cave. and freeze.")
    time.sleep(4)
    print('''You squint into the darkness and
simultaneously, the head of a dragon appears...''')
    time.sleep(4)
    print("You try to run away but trip over some metal objects.")
    time.sleep(4)
    print('''You scramble as quickly as possible away from the dragon
as it makes its way towards you.''')
    time.sleep(4)
    print("But...you are much too slow.")
    print('''The scaly dragon looms over you and stands up tall.
You watch in dread as the dragon opens its mouth, reveals its pointy teeth,
and...''')
    time.sleep(6)
    print()
    time.sleep(3)
    friendly_dragon = random.randint(1, 2)
    if cave_chosen == str(friendly_dragon):
        print("GIVES YOU A RIDE ON HIS BACK AND OFFERS ALL HIS TREASURES!")
        score += 1
        print()
        accept_treasure = random.randint(1, 2)
        print("You are offered all his treasures. Do you accept? (y or n)")
        while accept_treasure != "y" and accept_treasure != "n":
            accept_treasure = input()
        if accept_treasure == "y" and accept_treasure == y:
            print("So greedy!!")
        else:
            print("So generous!!")
    else:
        print("HE CHASES YOU AROUND, TRYING TO FART FIRE ON YOU!")
        dodge_fart = random.randint(1, 2)
        print("You try to escape his fiery fart. You jump...(l or r)")
        dodge_fart = input()
        if dodge_fart == "r" and dodge_fart == "r":
            print("You successfully escaped the fart!")
            print('''On the contrary, some of the shiny treasures in your pocket falls,
but at least you are alive.''')
        else:
            print("You got hit with the stinkest fart ever! You faint and never wake up!")
        dodge = input()
        if score >= 1:
            score -= 1
        
def play():
    stillPlaying = True
    while stillPlaying:
        show_intro()
        cave = choose_cave()
        check_cave(cave)
        print("Would you like to play again? (y to continue, q to quit)")
        choice = input()
        if choice == "q":
            stillPlaying = False
    print("Your score: " + str(score))
    print("Goodbye! Thanks for playin', naaamean?")

# Play the game!
play()




