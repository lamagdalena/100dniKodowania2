zbior_liczb = []

for x in range(2000, 3201):
    if x % 7 == 0 and x % 5 != 0:
        zbior_liczb.append(x)
        
print(zbior_liczb)