# map-reduce-SandeepNadendla
This is practice for map and reduce using python.

## Data Description:
- I took data about Olympics from ***[Kaggle](https://www.kaggle.com)*** 
- My data is about Medals gained by athlets and countries

## Study:
- I want to count the number of gold medals gained by each country.

## Execution:
- A ***Mapper Script*** extracts the countries, years, medals from each row in the dataset, which is used as a ***Key*** and a ***Value***. This is given as input to the ***Sorter*** which sorts all the countries. Based on the output of the Sorter, which is passed as input to the ***Reducer Script***, combines all the medal count.

## Powershell Command:
- ***cat summer.csv | python 21mapper.py | sort | python  23reducer.py > output21.txt***

## Summary:
- From the chart i get to know that us, Hun and Rus got more medals


![image](https://github.com/sandeepnadendla-git/map-reduce-nadendla/blob/main/Chart.PNG)
