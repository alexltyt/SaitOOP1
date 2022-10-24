"""5.	List:Write a Python program to create a list by concatenating a given list which range goes from 1 to n.  """

list1 = ['p', 'q']
n = 5
first_element = list1[0]
second_element = list1[1]
list2 = []
for i in range(n):
    list2.append(list1[0]+str(i+1))
    list2.append(list1[1]+str(i+1))
print(list2) 