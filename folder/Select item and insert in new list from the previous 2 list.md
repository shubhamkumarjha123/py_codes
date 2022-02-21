# With two provided list create one list such that new list contain only odd numbers from the first list and even number from the second list



```python
def merg(One, Two):
    print("First ", One)
    print("Second ", Two)
    thirdList = []
    
    for i in One:
        if (i % 2 != 0):
            thirdList.append(i)
    for i in Two:
        if (i % 2 == 0):
            thirdList.append(i)
    return thirdList

One = [4, 5, 22, 17, 62]
Two = [16, 1, 2, 7, 44]

print("result List is", merg(One, Two))
```

    First  [4, 5, 22, 17, 62]
    Second  [16, 1, 2, 7, 44]
    result List is [5, 17, 16, 2, 44]
    


```python

```
