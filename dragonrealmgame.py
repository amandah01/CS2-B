# Dragon Realm Midterm
# A game by Amanda Huynh
# December 22, 2017
# import stuff
import random
import time
# Global Variables
score = 0
Bag1 = {'Flask of Enchancement and Enhancement','Clementine Sword of the Breathern'}
Bag2 = {'Cloak of Dryaden Invisibility','Staff of Jokes'}
itemsOnPerson = '' 
# Show Introduction
def show_intro():
    print('''You've lost your map and there seems to be
no trace of the merchant's caravan you stowed away on. You see two path
diverging into different caves, both of which are dark and gloomy. ''')
    print()
    print('''You see a dark figure where the two paths diverge. You tentatively
approach.''')
    time.sleep(2)
    print('''Before you even reach the figure, you hear a voice. It is apparent
that the voice is from the stranger. You realize the figure is not a person,
but a dryad.''')
    time.sleep(3)
    print('''"Hi there! Who are you? Where are you from? What are you doing here
in the middle of no where? Are you lost? Do you need help? Huh? Huh?"''')
    time.sleep(3)
    print('''You are shocked into silence, for you have never seen a dryad behave
in such a friendly, though nosy, manner.''')
    time.sleep(2)
    def player_response():
        player_response = ""
    print('''You finally break out of your silence and open your mouth to speak.
What do you say? (1 or 2)
1) I'm a nobody from no where in particular. I have lost my sense of
direction.
2) You're annoying. Who are YOU? ''')
    while player_response != "1" and player_response != "2":
        player_response = input()
        if player_response == "1":
            print('''I'm a nobody from no where in particular. I have lost my sense of
direction.''')
            print()
            time.sleep(2)
            print('''"Oh no! Is that so? I am unable to provide you any help because
I have never left this secluded place. I am the guardian of these two caves.
In one cave, the dragon is friendly and will share his treasure with you.
The other dragon is malicious and menacing, and will eat you on site.
Although I cannot provide any knowledgable information beyond this,
I can offer you some weapons. ''')
            print()
        else: print('''You're annoying. Who are YOU?
I'm the guardian of these caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon is
malicious and menacing, and will eat you on site. You're going to need weapons
for protection. Luckily, I have some. However, you have to ask POLITELY. :) ''')
    time.sleep(2)
    print('''You contemplate this throughly and suppress a sigh. You have no other option
but to trust the dryad.''')
    time.sleep(3)
    print('''May you please provide me with some weapons for my journey, you magnificent
dryad?''')
    time.sleep(3)
    print('''The flattery seems to have worked. The dryad smiles and says," What
weapons do you desire?" ''')
    time.sleep(2)
    def weapon_response():
        weapon_response = ""
    print('''The dryad offers you two bags. Which do you choose? (1 or 2)
Bag 1 Contents: Flask of Enchancement and Enhancement and Clementine Sword of the Breathern.
Bag 2 Contents: Cloak of Dryaden Invisibility and Staff of Jokes''')
    while weapon_response != "1" and weapon_response != "2":
        weapon_response = input()
        if weapon_response == "1":
            print('''Here is Bag 1. Item 1: The Flask of Enchancement and Enhancement
can spell bound any enemies you face or enhance your fighting and defense abilities.
Item 2: The Clementine Sword of the Breathern will call upon ghosts to help you fight against
evils.''')
        else:
            print('''Here is Bag 2. Item 1: The Cloak of Dryaden Invisibility has been passed
down through generations of dryads. You will remain invisible the moment you cover yourself.
Unlike any normal cloak, it will not slip off of you unless you command it to. Item 2: The Staff of
Jokes will make your enemy stop in its tracks and start telling jokes. It is bounded until
you command your enemy to stop.''')
    return weapon_response
    return player_response
print()
time.sleep(5)
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
    time.sleep(3)
    print("You walk deeper into the cave and see MAGNIFICENT piles of TREASUREEEE!!")
    time.sleep(3)
    print('''You jump around and scream for joy!
You grab handfuls of stolen treasure and stuff them into your pockets and bag.''')
    time.sleep(4)
    print()
    print("Suddenly, you hear loud thumps at the back of the cave. and freeze.")
    time.sleep(3)
    
    def choose_item():
        chosenItem = ''
        print('''You decide to use:''')
        time.sleep(2)
        while chosenItem not in Bag2:
      
            for item in Bag2:
                print(" "+item)
                time.sleep(1)
                print()
            print('What item do you pick up?')
            chosenItem = input()
        print('You have chosen:', chosenItem)
        return chosenItem
    choose_item()
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
        score += 5
        print()
        accept_treasure = random.randint(1, 2)
        print("You are offered all his treasures. Do you accept? (y or n)")
        while accept_treasure != "y" and accept_treasure != "n":
            accept_treasure = input()
            if accept_treasure == "y":
                print("So greedy!!")
                score += 1
            else:
                print("So generous!!")
                score += 800
    else:
        print("HE CHASES YOU AROUND, TRYING TO FART FIRE ON YOU!")
        dodge_fart = random.randint(1, 2)
        print("You try to escape his fiery fart. You jump...(l or r)")
        dodge_fart = input()
        if dodge_fart == "r" and dodge_fart == "r":
            print("You successfully escaped the fart!")
            time.sleep(2)
            print('''On the contrary, some of the shiny treasures in your pocket falls,
but at least you are alive.''')
            score += 3
            time.sleep(2)
            print('''The dragon attempts to chase you again. What do you do? (1 or 2)
1. Use your item
2. Run''')
        else:
            print("You got hit with the stinkest fart ever! You faint and never wake up! Press Enter to Continue")
            score += -800
        dodge = input()
        if score >= 1:
            score -= 1
        
def play():
    stillPlaying = True
    while stillPlaying:
        show_intro()
        cave = choose_cave()
        check_cave(cave)
        print("Would you like to play again? (y to play again, q to quit)")
        choice = input()
        if choice == "q":
            stillPlaying = False
    print("Your score: " + str(score))
    print("Goodbye! Thanks for playing!")
# Play the game!
play()
