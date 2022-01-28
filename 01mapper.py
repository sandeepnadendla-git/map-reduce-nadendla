# Sandeep Nadendla
# Example mapper

inFile = open("purchases.txt","r")  # open file, read-only
outFile = open("output01.txt", "w") # open file, write
for line in inFile:  
    rowList = line.strip().split("    ") 
    # print (rowList )
    # print (len(rowList ))
    if len(rowList) == 6:
        date, time, location, dept, amount, payType = rowList  #assign names
        # print ("{0}\t{1}".format(location, amount))
        outFile.write("{0}\t{1}\n".format(location, amount))
inFile.close()
outFile.close()