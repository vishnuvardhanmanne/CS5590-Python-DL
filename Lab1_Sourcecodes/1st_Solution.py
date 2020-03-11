import itertools
# creating an empty list
Elements_list = []
# number of elements as input
n = int(input("Enter the number of elements of array: "))
print("Enter the values for elements:")
# iterating till the range
for i in range(0, n):
    elements = int((input()))
# adding the elements to the Elements_list
    Elements_list.append(elements)
for i in range(1,len(Elements_list)+1):
# Prints all possible combinations of r elements in a given array of size n
   a = (list(itertools.combinations(Elements_list,i)))
   print(list(set(a)))