#! usr/bin/env python3
# Fibonacci series

def main():
    a = 0
    b = 1
    ran = get_input()
    print_series(ran, a, b)


def get_input():
    num_range = int(input("please enter the range of the fibonacci series :"))
    return num_range


def print_series(num_range, a, b):
    for num in range(num_range):
        c = a + b
        print(b)
        a = b
        b = c


if __name__ == '__main__':
    main()
