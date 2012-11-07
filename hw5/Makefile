# Makes exprtest
CC=g++
CFLAGS=-Wall -g 

all: exprtest

exprtest: parser.tab scanner.cpp exprtest.o driver.o scanner.o
	$(CC) $(CFLAGS) exprtest.o driver.o parser.tab.cpp scanner.o -o exprtest


exprtest.o: exprtest.cpp
	$(CC) $(CFLAGS) -c exprtest.cpp

driver.o: driver.cpp
	$(CC) $(CFLAGS) -c driver.cpp

scanner.o: scanner.cpp 
	$(CC) $(CFLAGS) -c scanner.cpp

parser.tab: 
	bison parser.ypp

scanner.cpp: 
	flex -t scanner.ll > scanner.cpp

clean:
	rm -r *.o exprtest scanner.cpp parser.tab.cpp parser.tab.hpp
	
