#!/usr/bin/env python2

import csv

""" Converts a string read from a file or stdin to a dictionary """
def lineToDict(line):
    for row in csv.reader([line]):
        return {'id': row[0], 'desc': row[1], 'form': row[2], 'qty': row[3]}

""" Converts a dictionary object back into a CSV-separated string """
def dictToLine(dict):
    string = ""
    for key in ['id', 'desc', 'form', 'qty']:
        string += dict[key]
        string += ","
    return string.rstrip(",")

    
