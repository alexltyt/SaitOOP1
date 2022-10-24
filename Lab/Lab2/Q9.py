column = 0
row = 9

for rows in range(row):
    for columns in range(column):
        print("*", end="")
    print("*")
    if rows < 4:
        column +=1
    else:
        column -=1