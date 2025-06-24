#!/usr/bin/env python3

def add_one(num):
    return num + 1

num = 5
print("initial value of num:", num)

add_one(num)

print("value of num after calling add_one:", num)
# It does not add the value since the function only return the modified value, NOT the updated value itself.