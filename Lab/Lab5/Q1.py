"""Q1. Write a Python program to get a string made of the first 2 and the last 2 chars 
from a given a string. If the string length is less than 2, return instead of the empty string."""

print("Please enter a string, I will repeat your first and last 2 characters.")

input_string = input("Sample String :")
if len(input_string) < 2:
    print("Empty String")
else:
    print(f"Expected Result : {input_string[0:2]}", end="")
    print(input_string[-2:])
