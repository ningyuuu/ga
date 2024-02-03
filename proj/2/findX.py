# -*- coding: utf-8 -*-

"""

findX.py - Intro to Graduate Algorithms, Spring 2024

Solve the findX in an Infinite array problem (DPV 2.16) using a Divide & Conquer method
Your runtime must be O(log n)

The array of values is indexed A[1..<infinity>] inclusive

Your code MUST NOT directly reference any variables in findX.  The following methods are available for your use:
    
    findX.start(seed) -- returns the value (x) to search for within the array; (used in main but available for testing)
    findX.lookup(i) -- returns A[i] or None if i>n
    findX.lookups() -- returns the number of calls to lookup

""" 
#argparse allows the parsing of command line arguments
import argparse
#utility functions for cs 6515 projects
import GA_ProjectUtils as util


def findXinA(x, findX):

    #TODO Your Code Begins Here, DO NOT MODIFY ANY CODE ABOVE THIS LINE

    theIndex = None # replace None with the index of x
    lowerIdx = 1
    upperIdx = 1

    upperVal = None
    foundStart = False

    while not foundStart and theIndex is None:
        upperVal = findX.lookup(upperIdx)

        if upperVal == x:
            theIndex = upperIdx
        elif upperVal is not None and upperVal < x:
            lowerIdx = upperIdx
            upperIdx *= 2
        else:
            foundStart = True

    while theIndex is None:
        lookupIdx = (upperIdx + lowerIdx) // 2

        if (upperIdx - 1) == lowerIdx and lookupIdx == lowerIdx:
            break

        lookupVal = findX.lookup(lookupIdx)

        if lookupVal == x:
            theIndex = lookupIdx
        elif lookupVal is None or lookupVal > x:
            upperIdx = lookupIdx
        else:
            lowerIdx = lookupIdx

    #TODOne Your code Ends here, DO NOT MOIDFY ANYTHING BELOW THIS LINE

    numLookups = findX.lookups()

    return theIndex, numLookups


def main():
    """
    main - DO NOT CHANGE ANYTHING BELOW THIS LINE
    """
    # DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    parser = argparse.ArgumentParser(description='Find X')

    #args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument('-a', '--autograde',  help='Autograder-called (2) or not (1=default)', type=int, choices=[1, 2], default=1, dest='autograde')
    parser.add_argument('-s', '--seed', help='seed value for random function', type=int, default=1234, dest='seed')
    parser.add_argument('-l', '--nLower', help='lower bound for n', type=int, default=10, dest='nLower')
    parser.add_argument('-u', '--nUpper', help='upper bound for n', type=int, default=100000, dest='nUpper')

    args = parser.parse_args()

    #DO NOT MODIFY ANY OF THE FOLLOWING CODE

    findX = util.findX()
    x = findX.start(args.seed, args.nLower, args.nUpper)
    index, calls = findXinA(x, findX)
    print(f'findX result: x={x} found at index {index} in {calls} calls')

    return

if __name__ == '__main__':
    main()
