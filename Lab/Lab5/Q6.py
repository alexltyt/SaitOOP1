"""6.	Dictionary: Write a Python script to print a dictionary 
where the keys are numbers between 1 and 15 (both included) and 
the values are square of keys.  Sample Dictionary"""

dict1 = {}
for i in range(15):
    dict1[i+1]=(i+1)**2

print(dict1)
