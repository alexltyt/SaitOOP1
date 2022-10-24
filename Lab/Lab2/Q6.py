start = 25
end = 50
nonprime = False #default the number is not a prime

for a in range(start, end): #get the numbers between start and end as a
    for i in range(2,a): #get the numbers between 2 and a as i
        if (a % i) == 0: # if a can be divided by i, it is not a prime
            nonprime = True
            break
    if not nonprime:
        print(a)    # print the result
    nonprime = False #reset the boolean
        
    