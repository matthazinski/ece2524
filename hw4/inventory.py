#!/usr/bin/env python2

import sys
import argparse
import parserecord
database = []

def main():
    global args
    parser = argparse.ArgumentParser(description='Inventory management interface.')
    parser.add_argument("--datafile", help="path to the data file to read at startup")
    args = parser.parse_args()

    #database = [] # store data as a list of dictionaries

    if args.datafile:
        useFile = 1
        print "Data file detected!"
        file=open(args.datafile)
        for line in file:
            entry = parserecord.lineToDict(line)
            database.append(entry)
            # TODO call add() function
        file.close()
    
    else:
        useFile = 0
        print "Warning! Changes will not be saved to a file!"
    
#    print "Current inventory:"
#    for line in database:
#        print line

    commands = iter(sys.stdin.readline, '')
    for line in commands:
        # TODO read from stdin
        parseInput(line)


    #data = iter(sys.stdin.readline, '')
    #for line in data:
        

def parseInput(line):
    line = line.replace("\t", " ")
    cmd = line.split(" ")[0]
    data = line.replace(cmd,"").strip()
    if (cmd == 'add'):
        # Syntax: "add id,description,footprint,quantity"
        dict = parserecord.lineToDict(data)
        database.append(dict)
        print dict['id'], " has been added"
        writeToFile(database)
        return    
    if (cmd == 'remove'):
        # Syntax: "remove id"
        # Set the database equal to the database except IDs that should be
        # removed
        database[:] = [d for d in database if d.get('id') != data]
        print id, " has been removed"
        writeToFile(database)
        return
    if (cmd == 'list'):
        # Syntax: "list key value"
        # Get key and value
        key = data.split(" ")[0]
        value = data.replace(key,"").strip()
        if (key == "all"):
            for item in database:
                print parserecord.dictToLine(item)
        else:
            for item in [d for d in database if d.get(key) == value]:
                print parserecord.dictToLine(item)
        return
            
    # Check for invalid commands
    print "Invalid command!"


""" Write the database to disk, overwriting the file. """
def writeToFile(db):
    global args
    f = open(args.datafile, 'w')
    for entry in db:
        f.write(parserecord.dictToLine(entry))
        f.write("\n")
    f.close()

if __name__ == '__main__':
    main()
