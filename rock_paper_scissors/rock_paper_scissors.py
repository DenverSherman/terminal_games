import random
print("Let's play Rock Paper Scissors!")
play_again = "Y"
options = ['r','p','s']
options_dict = {'r':'rock', 'p':'paper', 's':'scissors'}
conditions_dict = {'r': 1, 'p': 2, 's': 3}
user_win_count = 0
computer_win_count = 0

#loop back here
while play_again == "Y" or play_again == "y":
    selection = input("Make your Choice: (r)ock, (p)aper, or (s)cissors?\n")
    computer_selection = random.choice(options)

    #error loop
    while selection != 'r' and selection != 'p' and selection != 's':
        selection = input("Please choose from 'r', 'p', 's'\n")
    
    #show hands
    print(f"You picked {options_dict[selection]}. The computer picked {options_dict[computer_selection]}.")

    #test results
    if conditions_dict[selection] == conditions_dict[computer_selection]:
        print("It's a tie!")
    elif (conditions_dict[selection] + 2) % 3 == conditions_dict[computer_selection] % 3:
        print("You won! Take that, computer!")
        user_win_count += 1
    else:
        print("You lost!")
        computer_win_count += 1
    print(f"You: {user_win_count} - Computer: {computer_win_count}")

    #restart loop (maybe)
    play_again = input("Press [Y] to play again!\n")