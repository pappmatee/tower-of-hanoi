#!/usr/bin/env python3

rod_one = [3, 2, 1]
rod_two = []
rod_three = []

rods = [rod_one, rod_two, rod_three]

def isGoalState():
    return rod_three == [3, 2, 1]


def isValidOperation(where, to):
    if len(to) == 0:
        minimum = 4
    else:
        minimum = min(to)
 
    return len(where) != 0 and where != to and min(where) < minimum


def put(where, to):
    if not(isValidOperation(where, to)):
        print("The requested operation is not valid...")
        return False
    
    value = where.pop()
    to.append(value)


def printState():
    print("###############")
    print("1: " + str(rod_one))
    print("2: " + str(rod_two))
    print("3: " + str(rod_three))
    print("###############")


def main():
    printState()

    while(not(isGoalState())):
        input_where = input("Honnan: ")
        input_to = input("Hova: ")

        where = rods[int(input_where) - 1]
        to = rods[int(input_to) - 1]

        put(where, to)

        printState()



################################

if __name__ == "__main__":
    main()