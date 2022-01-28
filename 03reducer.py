# Sandeep Nadendla
# sorter Example



inFile = open("sorted01.txt","r")  # open file, read-only
outFile = open("reduced01.txt", "w") # open file, write

thisKey = ""
thisValue = 0.0

for line in inFile:
  data = line.strip().split('\t')
  store, amount = data
  if store != thisKey:
    if thisKey:

      # output the last key value pair result
      outFile.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done
outFile.write(thisKey + '\t' + str(thisValue)+'\n')

inFile.close()
outFile.close()