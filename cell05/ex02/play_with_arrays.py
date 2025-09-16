#!/usr/bin/env python3

num = [2, 8, 9, 48, 8, 22, -12 ,2]
print(num)
n_num = []
for i in num:
    if i + 2 > 5:    
        i = i + 2
        n_num.append(i)
    else:
        continue

print(n_num)