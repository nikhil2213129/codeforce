from collections import Counter

def is_amusing_joke(name1, name2, joke):
    combined_name = name1 + name2
    return Counter(combined_name) == Counter(joke)

name1 = input().strip()
name2 = input().strip()
joke = input().strip()

if is_amusing_joke(name1, name2, joke):
    print("YES")
else:
    print("NO")
