""" 3.	Write a Python program to find the first appearance 
 of the substring 'not' and 'poor' from a given string, 
 if 'not' follows the 'poor', replace the whole 'not'...
 'poor' substring with 'good'. Return the resulting string."""

enterString = "The lyrics is not that poor!"

finder_not = enterString.find("not")
finder_poor = enterString.find("poor")

if finder_poor != -1 and finder_not != -1 and finder_poor>finder_not:
    enterString = enterString.replace("poor","good")
    enterString = enterString.replace(" not that","")
    print(enterString)
else:
    print("The lyrics is poor.")
