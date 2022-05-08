#!usr/bin/env python3
# Program to find the version of python used

import platform  # this imports the details on the version


def using_format():
    # This line is used to print the version of the program
    print('The version of python used in this program is : {}'.format(platform.python_version()))


def using_f():
    # This line also prints the version of the python used
    print(f'The version of python used in this program is : {platform.python_version()}')


def main():
    using_format()
    using_f()


# If condition forces the interpreter to read the complete program before execution
if __name__ == '__main__':
    main()
