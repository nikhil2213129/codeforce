n = input()
ch = ""
d = []
for i in range(len(n)):
    if n[i] == '+':
        ch = int(ch)
        d.append(ch)
        ch = ""
    else:
        ch += n[i]
    if i == len(n)-1:
        ch = int(ch)
        d.append(ch)
d.sort()
ch = ""
for i in d:
    ch = ch + str(i) +"+"
print(ch[:len(ch)-1])
    
