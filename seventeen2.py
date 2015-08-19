#!/usr/bin/env python
# seventeen Version 2
# Author: Pooja Jain
# Last edits: 19.08.2015
# The program reads from an input file (named 'i206_placein_input.txt')
# a sequence of comma delimited numbers representing the sequence of 
# moves made by Player 1. Each line of the input file represents a 
# different game. For example, the sample input file contains data for 
# ten games. In the first game, Player 1 removes 3 marbles during its 
# first turn, 1 marble during its second turn, three marbles during its 
# third turn, and so on.
# 
# If the number of marbles left in the jar is fewer than the next number
# in the play sequence, then Player 1 should remove all the remaining 
# marbles. For example, if there are two marbles left in the jar, and 
# the next number in the sequence is 3, then Player 1 should remove two 
# marbles, not three

#imports
from random import randint

#body
   
def human_turn(number, total):
    num = int(number)
    if(num > total) :
        total = 0
    else :
        total = total - num

    return total


def computer_turn(Total_marbles):
    comp_num = randint(1,3)
    if comp_num > Total_marbles:
        Total_marbles = 0
    else:
        Total_marbles = Total_marbles - comp_num   
    return Total_marbles
    
    
    
def main():
    
    count = 1
    player1WinCount = 0
    player2WinCount = 0
    
    outfile = open("i206_placein_output2.txt", 'w')
    infile = open("i206_placein_input.txt")
    
    for lines in infile:
        Total_marbles = 17
#         
        playerPattern = ""
        line = lines.replace('\n', ' ').replace(',',' ').split()
        
        for number in line:
            Total_marbles_human = human_turn(number, Total_marbles)
            if(Total_marbles_human == 0) :
                playerPattern +=  number + '-'
                winner="P2"
                player2WinCount += 1
                break
            
            Total_marbles = computer_turn(Total_marbles_human)
            playerPattern +=  number + '-' + str(Total_marbles_human-Total_marbles) + '-'
            
            if (Total_marbles == 0):
                winner = "P1"
                player1WinCount += 1
                break
            
            if(Total_marbles > 0) :
                continue 
        
        outputSequence = "Game #" + str(count)+ ". Play sequence: " + playerPattern[: -1]  + ". " +  "Winner: " + winner + "\n"    
        count += 1
        outfile.write(outputSequence)
    outfile.write("Player 1 won {0} times; Player 2 won {1} times." .format(player1WinCount, player2WinCount))
            
    infile.close()
    outfile.close()    
            
if __name__ == '__main__':
    main()
        