#!/usr/bin/env python3
"""CHALLENGE: Range Practice"""

while True:
    try:
        bottles = int(input("Choose a number between 1 and 99: "))
        if bottles < 1: 
            print("Enter a number greater than 0")
        elif bottles > 99:
            print("Enter a number less than 100")
        else:
            break
    except ValueError:
        print("Please enter a valid integer. ")

for i in range(bottles, 0, -1):
    if i == 1:
        plural = ""
    else:
        plural = "s"
    print(f"{i} bottle{plural} of beer on the wall!")
    print(f"{i} bottle{plural} of beer! You take one down, pass it around!")
    if i-1 == 1:
        plural = ""
        remaining_bottles = " bottle"
    elif i-1 == 0:
        remaining_bottles = "no more bottles"
    else:
        plural = "s"
        remaining_bottles = str(i-1) + " bottles"
    print(f"{i-1} {remaining_bottles} of beer on the wall!\n")
