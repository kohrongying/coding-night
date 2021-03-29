# Session 1

## TODO
Write a program that given a number (with arbitrary number of digits), converts it into LCD style numbers using the following format:
```
    _   _       _   _   _   _   _  
 |  _|  _| |_| |_  |_    | |_| |_|  
 | |_   _|   |  _| |_|   | |_|  _|  
```

  
(each digit is 3 lines high)

Give your programme two addition variables height and width:
For example, for digit 2 with height=2, width=3 will be like
```
 ___
|   |
|___|
|   |
|___|
```  
(the height consists of 2 lines and weight for 3 lines)

## HOW TO RUN
```
python ./session-1/main.py 9659 

python ./session-1/main.py 1212 -w 3 -ht 1
```