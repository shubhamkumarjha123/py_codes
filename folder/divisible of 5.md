# For a list print which are divisible of 5


```python
def fndDiv(numList):
    print("Given list is ", numList)
    print("Divisible of 5 in a list")
    for num in numList:
        if (num % 5 == 0):
            print(num)

List =[5, 43, 22, 75, 29]
fndDiv(List)
```

    Given list is  [5, 43, 22, 75, 29]
    Divisible of 5 in a list
    5
    75
    
