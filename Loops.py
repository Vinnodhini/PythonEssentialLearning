#!usr/bin/env python3
# This is a sample program to demonstrate loops

# Defining a list
test = ['Ramanan', 'Santhi', 'Aanandh', 'Vinnodhini', 'Vikraant', 'Adirant']


# Calling the main function
def main():
    for_loop()
    print()
    for_loop_range()
    print()
    while_loop()


# This is used to print the list of name using for Loop
def for_loop():
    for names in test:
        print(names)


# This is used to print the list of names with for loops and indexes
def for_loop_range():
    for num in range(6):
        print(test[num])


# This is used to print list of names using while loops
def while_loop():
    x = 0
    while x < 6:
        print(test[x])
        x += 1


if __name__ == '__main__':
    main()
