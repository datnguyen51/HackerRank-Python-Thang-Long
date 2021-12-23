#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):
    string = ''
    for i in range(len(s)):
        if i == 0:
            string += s[i].upper()
        elif s[i-1] == ' ':
            string += s[i].upper()
        else:
            string += s[i]

    return string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
