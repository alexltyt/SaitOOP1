"""7.	Tuple: Write a Python program to replace last value of tuples in a list. """

list1 =  [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

part1 = list(list1[0])
part2 = list(list1[1])
part3 = list(list1[2])

list3 = [(part1),(part2),(part3)]
for i in range(len(list3)):
    list3[i][2] = int(100)

print(list3)

#print([t[:-1] + (100,) for t in l])