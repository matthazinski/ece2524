#!/usr/bin/env python2
# ECE 2524 Homework 2 Problem 3 Matt Hazinski
with open('account', 'r') as f:
    
    total = 0.0
    maximum = 0.0
    minimum = float("inf")
    numAccounts = 0
    minPerson = ""
    maxPerson = ""
    print "ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS"
    
    for line in f:
        # Convert tabs to spaces
        line = line.replace("\t", " ")
        
        first = line.split(" ")[0];
        line = line.replace(first, " ").strip()

        last = line.split(" ")[0];
        line = line.replace(last, " ").strip()

        amount = line.split(" ")[0]
        amountF = float(amount)
        line = line.replace(amount, " ").strip()

        total = total + amountF
        numAccounts = numAccounts + 1

        if amountF > maximum: 
            maximum = amountF
            maxPerson = last
        if amountF < minimum:
            minimum = amountF
            minPerson = last

        city = line.split(" ")[0]
        line = line.replace(city, " ").strip()

        phone = line
        
    print "ACCOUNT SUMMARY"
    print "Total amount owed = " + str(total)
    print "Average amount owed = " + str(total/numAccounts)
    print "Maximum amount owed = " + str(maximum) + " by " + maxPerson
    print "Minimum amount owed = " + str(minimum) + " by " + minPerson
