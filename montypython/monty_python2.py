#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   CHALLENGE 01 & 02 - Solutions to both challenges."""

#counter to control while loop
round = 0

while True:     #sets up an infinite loop condition
    #Increment counter by 1
    round = round +1
    
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer = input("Your guess --> ")   # string ans collected from user

    if answer == 'Brian':  #logic to check if user gave correct answer
        print('Correct')
        break   # break statement escapes the while loop

    elif round == 3:   #logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
        break # break statement escapes the while loop

    else: # if answer was wrong, and round is not yet equal to 3
        print("Sorry! Try again!")

