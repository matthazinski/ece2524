#!/usr/bin/env python2
# ECE 2524 Homework 2 Problem 1 Matt Hazinski
with open('/etc/passwd', 'r') as f:
    for line in f:
        line = line.rstrip()
        user = line.split(':')[0]
        shell = line.split(':')[6]
        print user + "\t" + shell

