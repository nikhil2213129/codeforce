borze = input()
i = 0
ans = ""
while i < len(borze):
    if borze[i] == '.':
        ans += '0'
        i += 1
    elif borze[i:i+2] == '-.':
        ans += '1'
        i += 2
    elif borze[i:i+2] == '--':
        ans += '2'
        i += 2
print(ans)
