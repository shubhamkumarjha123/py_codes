# Given a list of numbers, return True if first and last number of a list is same


```python
def check_if_First_And_Last_Same(numberList):
    print("Given list is ", numberList)
    firstElement = numberList[0]
    lastElement = numberList[-1]
    if (firstElement == lastElement):
        return True
    else:
        return False

numList = [10, 20, 30, 40, 10]
print("result is", check_if_First_And_Last_Same(numList))
```

    Given list is  [10, 20, 30, 40, 10]
    result is True
    
