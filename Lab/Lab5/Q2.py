"""2.	Write a Python program to get a string from a given string where all 
 occurrences of its first char have been changed to '$', except the first 
 char itself. """

print("Please enter a string, I will change the first character to $.")

input_string = input("String: ")
firstchar = input_string[0]
result = input_string.replace(input_string[0],"$")
print(f"{firstchar}{result[1:]}")