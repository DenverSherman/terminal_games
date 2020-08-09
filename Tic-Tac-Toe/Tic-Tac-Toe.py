print("Welcome to my tic-tac-toe game")

bar = "___|___|___"
end_bar = "   |   |   "
#replace numbers 0 - 8 with a list
#change items in list based on inputs
#Check if the current inputs match a win condition]
#if yes, "get dunked on"
#if no, restart

#steps for improvement:
#Don't ask to play again if you say no
#Win Condition = TRUE, print("Gratz"), stop game, play again
#No entries overwrite (tuples?)
#Develop winning Tic-Tac-Toe Algorithm (AI)

entries = [1,2,3,4,5,6,7,8,9]

#print the board state

print("",entries[0],"|",entries[1],"|",entries[2])
print(bar)
print("",entries[3],"|",entries[4],"|",entries[5])
print(bar)
print("",entries[6],"|",entries[7],"|",entries[8])
print(end_bar)
play_again = "Y"
initiate = input("Would you like to play a game? [Y/N] ")

while play_again == "Y":
    if initiate == "Y":
        turn_counter = 1
        while turn_counter <= 9:
            # if even/odd turn to determine X or O inputs
            if turn_counter % 2 == 1:
                position = int(input("Select a numbered square you'd like to be an X: "))-1
                entries[position] = "X"
            else:
                position = int(input("Select a numbered square you'd like to be an O: "))-1
                entries[position] = "O"
            #Print Board
            print("",entries[0],"|",entries[1],"|",entries[2])
            print(bar)
            print("",entries[3],"|",entries[4],"|",entries[5])
            print(bar)
            print("",entries[6],"|",entries[7],"|",entries[8])
            print(end_bar)
            #Next Turn
            turn_counter = turn_counter + 1
    play_again = input("Play again? [Y/N]: ")
    entries = [1,2,3,4,5,6,7,8,9]
    #Print Board
    print("",entries[0],"|",entries[1],"|",entries[2])
    print(bar)
    print("",entries[3],"|",entries[4],"|",entries[5])
    print(bar)
    print("",entries[6],"|",entries[7],"|",entries[8])
    print(end_bar)