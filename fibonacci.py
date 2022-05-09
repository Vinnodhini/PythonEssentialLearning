#! usr/bin/env python3
# Fibonacci series

a = 0
b = 1

num_range = int(input("please enter the range of the fibonacci series :"))

for num in range(num_range):
    c = a + b
    print(b)
    a = b
    b = c

