#!/usr/bin/python3.11
x = int(input("type your first element "))
y = int(input("type your second element "))
sub = x - y
if sub < 0:
    sub = 0 - sub
print(f"the sum is equal {sub / (x + y )}")
