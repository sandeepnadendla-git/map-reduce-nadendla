# Sandeep Nadendla
# sorter Example

# Case 2 - Reducer using standard input and output
# Easy to test locally in the terminal

import sys

thisKey = ""
thisValue = 0

for line in sys.stdin:  
  datalist = line.strip().split('\t')
  if (len(datalist) == 3) : 
    Year, Country, Medal = datalist

    if Country != thisKey:   # we've moved to another key      
      if thisKey:
        if Medal == "Gold":
        # output the previous key-summaryvalue result
          print(thisKey,'\t',thisValue)

      # start over for each new key
      thisKey = Country 
      thisValue = 0
   
    # apply the aggregation function
    thisValue  = thisValue + 1

# output the final key-summaryvalue result outside the loop
print(thisKey,'\t',thisValue)
