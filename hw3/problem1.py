#!/usr/bin/env python2
import sys
import argparse
parser = argparse.ArgumentParser(description='Multiply integers.')
args = parser.parse_args()

product = 1;
data = iter(sys.stdin.readline, '')
for line in data:
    try:
        product = product * int(line)
    except TypeError as te:
        sys.stderr.write(te)
        sys.exit(1)
    except ValueError as ve:
        break
print product
