import random;

options = ["rock", "paper", "scissors"]

npc = options[random.randint(0,2)]

score=0

game = True

while game == True:
    play = input("Rock, Paper, Scissors, shoot!").lower()
    if play == npc:
        print("It's a tie!")
    elif play == options[0]:
        if npc == options[1]:
            print("You lose!", npc, "covers", play)
            score=score-1
        else:
            print("You win!", play, "crushes", npc)
            score=score+1
    elif play == options[1]:
        if npc == options[2]:
            print("You lose!", npc, "cuts", play)
            score=score-1
        else:
            print("You win!", play, "covers", npc)
            score=score+1
    elif play == options[2]:
        if npc == options[0]:
            print("You lose!", npc, "crushes", play)
            score=score-1
        else:
            print("You win!", play, "cuts", npc)
            score=score+1
    else:
        print("Try that again...")

    again=input("Play again? (y/n)")
    if again == "y":
      game = True
      npc = options[random.randint(0,2)]
    else:
      game = False
    print("Your score:", score)
