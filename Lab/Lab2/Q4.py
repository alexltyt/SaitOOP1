number = float(input("please enter a number.")) #input a number
counter = 0 #counter start from 0

while number > 1: 
    print(number)
    number /= 10 #find how many digits
    counter += 1 #counter increase when the number can divided by 10

print(f"This number has {counter} digits.")