# Sandeep Nadendla
# Example mapper
import sys

for line in sys.stdin:
    rowList = line.strip().split(",") 
    if len(rowList) == 9:
        Year, City, Sport, Discipline, Athlete, Country, Gender, Event, Medal = rowList  #assign names
        
        # print intermediate key-value pairs to standard output
        print ("{0}\t{1}\t{2}\n".format(Year, Country, Medal))


