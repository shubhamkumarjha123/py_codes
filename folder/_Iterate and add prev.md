# Given a range of the first 50 numbers, Iterate from the start number to the end number, and In each iteration print the sum of the current number and previous no.


```python
def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current Number", i, "Previous Number ", previousNum ," Sum: ", sum)
        previousNum = i

print("Printing  current  and  previous  number  sum  in  a  given  range(50)")
sumNum(50)
```

    Printing  current  and  previous  number  sum  in  a  given  range(50)
    Current Number 0 Previous Number  0  Sum:  0
    Current Number 1 Previous Number  0  Sum:  1
    Current Number 2 Previous Number  1  Sum:  3
    Current Number 3 Previous Number  2  Sum:  5
    Current Number 4 Previous Number  3  Sum:  7
    Current Number 5 Previous Number  4  Sum:  9
    Current Number 6 Previous Number  5  Sum:  11
    Current Number 7 Previous Number  6  Sum:  13
    Current Number 8 Previous Number  7  Sum:  15
    Current Number 9 Previous Number  8  Sum:  17
    Current Number 10 Previous Number  9  Sum:  19
    Current Number 11 Previous Number  10  Sum:  21
    Current Number 12 Previous Number  11  Sum:  23
    Current Number 13 Previous Number  12  Sum:  25
    Current Number 14 Previous Number  13  Sum:  27
    Current Number 15 Previous Number  14  Sum:  29
    Current Number 16 Previous Number  15  Sum:  31
    Current Number 17 Previous Number  16  Sum:  33
    Current Number 18 Previous Number  17  Sum:  35
    Current Number 19 Previous Number  18  Sum:  37
    Current Number 20 Previous Number  19  Sum:  39
    Current Number 21 Previous Number  20  Sum:  41
    Current Number 22 Previous Number  21  Sum:  43
    Current Number 23 Previous Number  22  Sum:  45
    Current Number 24 Previous Number  23  Sum:  47
    Current Number 25 Previous Number  24  Sum:  49
    Current Number 26 Previous Number  25  Sum:  51
    Current Number 27 Previous Number  26  Sum:  53
    Current Number 28 Previous Number  27  Sum:  55
    Current Number 29 Previous Number  28  Sum:  57
    Current Number 30 Previous Number  29  Sum:  59
    Current Number 31 Previous Number  30  Sum:  61
    Current Number 32 Previous Number  31  Sum:  63
    Current Number 33 Previous Number  32  Sum:  65
    Current Number 34 Previous Number  33  Sum:  67
    Current Number 35 Previous Number  34  Sum:  69
    Current Number 36 Previous Number  35  Sum:  71
    Current Number 37 Previous Number  36  Sum:  73
    Current Number 38 Previous Number  37  Sum:  75
    Current Number 39 Previous Number  38  Sum:  77
    Current Number 40 Previous Number  39  Sum:  79
    Current Number 41 Previous Number  40  Sum:  81
    Current Number 42 Previous Number  41  Sum:  83
    Current Number 43 Previous Number  42  Sum:  85
    Current Number 44 Previous Number  43  Sum:  87
    Current Number 45 Previous Number  44  Sum:  89
    Current Number 46 Previous Number  45  Sum:  91
    Current Number 47 Previous Number  46  Sum:  93
    Current Number 48 Previous Number  47  Sum:  95
    Current Number 49 Previous Number  48  Sum:  97
    


```python

```
