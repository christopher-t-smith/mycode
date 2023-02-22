#!/usr/bin/env python3

#ask what is the hostname
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    #Code Customizations 01
    print("hostname matches expected config")

#Code Customization 02 and 03
print("exiting the script")
