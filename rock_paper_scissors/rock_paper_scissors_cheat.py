import random
print("Let's play Rock Paper Scissors!")
play_again = "Y"
options = ['r','p','s']
options_dict = {'p':'paper', 'r':'rock', 's':'scissors'}
conditions_dict = {'r': 1, 'p': 2, 's': 3}

#loop back here
while play_again == "Y" or play_again == "y":
    selection = input("Make your Choice: (r)ock, (p)aper, or (s)cissors?\n")
    #error loop
    while selection != 'r' and selection != 'p' and selection != 's':
        selection = input("Please choose from 'r', 'p', 's'\n")
    
    #winning loop
    computer_selection = random.choice(options)
    while (conditions_dict[selection] + 2) % 3 == conditions_dict[computer_selection] % 3:
        computer_selection = random.choice(options)
    
    #show hands
    print(f"You picked {options_dict[selection]}. The computer picked {options_dict[computer_selection]}.")

    #test results
    if conditions_dict[selection] == conditions_dict[computer_selection]:
        print("It's a tie!")
    else:
        print("You lost!")

    #restart loop (maybe)
    play_again = input("Press [Y] to play again!\n")