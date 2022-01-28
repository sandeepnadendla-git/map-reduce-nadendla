# Sandeep Nadendla
# sorter Example


inFile = open("output01.txt","r")  # open file, read-only
outFile = open("sorted01.txt", "w") # open file, write
lines = inFile.readlines()
lines.sort()

for line in lines:
	outFile.write(line)
inFile.close()
outFile.close()
