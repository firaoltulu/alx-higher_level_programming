#!/usr/bin/python3
"""
This queens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions.
"""


from sys import argv

if __name__ == "__main__":
    two = []
    if len(argv) != 2:
        print("Usage: function_four N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    one = int(argv[1])
    if one < 4:
        print("N must be at least 4")
        exit(1)

    for five in range(one):
        two.append([five, None])

    def function_one(ten):
        """This check that a queen does not already exist in that y value"""
        for x in range(one):
            if ten == two[x][1]:
                return True
        return False

    def function_two(ten, nine):
        """This determines whether or not to function_two the solution"""
        if (function_one(nine)):
            return False
        five = 0
        while(five < ten):
            if abs(two[five][1] - nine) == abs(five - ten):
                return False
            five += 1
        return True

    def function_three(ten):
        """This clears the answers from the point of failure on"""
        for five in range(ten, one):
            two[five][1] = None

    def function_four(ten):
        """This recursive backtracking function to find the solution"""
        for five in range(one):
            function_three(ten)
            if function_two(ten, five):
                two[ten][1] = five
                if (ten == one - 1):  
                    print(two)
                else:
                    function_four(ten + 1)  

    function_four(0)
