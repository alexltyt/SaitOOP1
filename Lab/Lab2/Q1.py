col_num = 1

for x in range(5): #total 5 row
    for i in range(col_num): #print i in each row
        print(i+1, end=" ")  #i+1 = start from 1;use end="" to avoid start a new line
    print("") #new line after finish printing i
    col_num += 1 #adding 1 column in each loop
        
    