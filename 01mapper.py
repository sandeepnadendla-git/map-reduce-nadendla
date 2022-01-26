# Sandeep Nadendla
# Example mapper

f = open("purchases.txt","r")           # open file, read-only
for line in f:  
    dataList = line.strip().split("    ")    # count the spaces!
    print (dataList   )
    print (len(dataList  ))
    if len(dataList  ) == 6:
        date, time, location, dept, amount, payType = dataList  #assign names
        print ("{0}\t{1}".format(location, amount))
f.close()
