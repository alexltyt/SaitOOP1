"""8.	Tuple: Write a Python program to remove an empty tuple(s) from a list of tuples. """


list1 =[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
list2 = []

for i in range(len(list1)):
    if list1[i]:       
        list2.append(list1[i])

print(list2)