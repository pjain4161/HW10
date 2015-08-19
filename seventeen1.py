#!/usr/bin/env python
# seventeen Version 1
# Author: Pooja Jain
# Last edits: 19.08.2015

# The program should allow a human to play against a computer. 
# The human always goes first. If the human enters incorrect input
# (anything other than 1, 2, 3, or a number larger than the number of marbles 
# remaining in the jar), an error message should be displayed, 
# and the human is prompted to try again.
# The computer player can choose to remove marbles according to 
# any strategy of your choosing. 
# At the end of each turn, the program should print out the number 
# of marbles removed in the previous turn, and the number of marbles 
# that remain in the jar. Once there are no more marbles in the jar, 
# the program should declare the winner of the game.

#imports
from random import randint

#body
def start_message():
    print "Let's play the game of Seventeen!"
    print "Number of marbles left in jar: 17"
    
    
def human_turn(total):
    
    num = raw_input("\nYour turn: How many marbles will you remove (1-3)? ")
    
    try:
        num_int = int(num)
        
    except:
        print "Sorry, that is not a valid option. Try again!" 
        print "Number of marbles left in jar: {0}" .format(total)
        num = human_turn(total)
        return num
        
    else:
        if ( ( num_int not in (1,2,3) ) or (num_int > (total) ) ):
            print "Sorry, that is not a valid option. Try again!"
            print "Number of marbles left in jar: {0}" .format(total)
            num = human_turn(total)
            return num
        else:
            num = int(num)
            total = total - num
            print "You removed {0} marbles." .format(num)
            print "Number of marbles left in jar: {0}" .format(total)
            return num
            
            

def print_message(Total_marbles, comp_num):
    Total_marbles = Total_marbles - comp_num
    print "Computer removed {0} marbles.".format(comp_num)
    print "Number of marbles left in jar: {0}".format(Total_marbles)
    return Total_marbles

def computer_turn(Total_marbles):
    comp_num = randint(1,3)
    if comp_num > Total_marbles :
        Total_marbles = computer_turn(Total_marbles)
        return Total_marbles
        
    Total_marbles = print_message(Total_marbles, comp_num)

    return Total_marbles
    
    
    
def main():
    Total_marbles = 17
    start_message()

    while(Total_marbles > 0):
        
        #Human Turn
        human_input = human_turn(Total_marbles)
        Total_marbles = Total_marbles - human_input
        
        if (Total_marbles == 0):
            winner = "Computer"
            break
        
        #Computer Turn
        print "\nComputer's turn..."
        Total_marbles = computer_turn(Total_marbles) 
        if (Total_marbles == 0):
            winner = "Player"
            break
        
        
    print "\nThere are no marbles left. {0} wins!" .format(winner)
    
if __name__ == '__main__':
    main()