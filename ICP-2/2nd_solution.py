def string_alternative(string):
    b = ""
    for i in range(len(string)):
        if(i%2)==0:
            b+=string[i]
    return b
print(string_alternative(string=str(input("enter a string:"))))