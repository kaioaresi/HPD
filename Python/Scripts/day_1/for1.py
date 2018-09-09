#!/usr/bin/env python3


for c in range(5,10):
    if c == 3:
        continue
    print(c)

print('='*10)

for c in range(5,10):
    if c == 3:
        break
    print(c)
