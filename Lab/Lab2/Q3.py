numbers = [12, 75, 150, 180, 145, 525, 50,40,32]

for i in numbers:  #loop the number array
    if i > 500:
        break #stop the loop when the number is great then 500
    if i % 5 == 0 and i <= 150 : #can be divided by 5 and not greater than 150
        if i > 150:
            break #skip and run the next loop when the number is greater then 150
        print(i)    
            
            
