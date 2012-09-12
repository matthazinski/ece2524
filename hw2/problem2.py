#!/usr/bin/env python2
# ECE 2524 Homework 2 Problem 2 Matt Hazinski
with open('account', 'r') as f:
    
    print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
    
    for line in f:
        # Convert tabs to spaces
        line = line.replace("\t", " ")
        
        first = line.split(" ")[0];
        line = line.replace(first, " ").strip()

        last = line.split(" ")[0];
        line = line.replace(last, " ").strip()

        amount = line.split(" ")[0]
        line = line.replace(amount, " ").strip()

        city = line.split(" ")[0]
        line = line.replace(city, " ").strip()

        phone = line
        
        print phone + ", " + last + ", " + first + ", " + amount
#        line = line.rstrip()
#        user = line.split(':')[0]
#        shell = line.split(':')[6]
#        print user + "\t" + shell

