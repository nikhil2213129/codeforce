"""
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis

"""

n = int(input())
d = []
for i in range(n):
    x = input()
    d.append(x)
for i in d:
    if len(i)<10:
        print(i)
    else:
        print(i[0] + str(len(i)-2) + i[len(i)-1])

    
    
