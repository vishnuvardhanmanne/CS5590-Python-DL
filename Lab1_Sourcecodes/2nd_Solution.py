# Create first dictionary
dict1 = {'Vishnu': 5, 'Vandith': 7, 'Jeswanth': 10}
# Create second dictionary
dict2 = {'Haneesh': 8, 'Vishnu': 20, 'Harun': 11}
# Merge contents of dict2 in dict1
dict1.update(dict2)
print('Updated dictionary 1 :')
print(dict1)
# Create a list of tuples sorted by index 1 i.e. value field
listofTuples = sorted(dict1.items(), key=lambda x: x[1])
# Iterate over the sorted sequence
for elem in listofTuples:
    print(elem[0], " ::", elem[1])
