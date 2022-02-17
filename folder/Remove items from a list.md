# Remove items from a taken list while iterating but without creating a different copy of a list  (Here remove no. greater than 70)


```python
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 0

n = len(number_list)
# iterate list till i is smaller than n
while i < n:
    # check if number is greater than 50
    if number_list[i] > 70:
        # delete current index from list
        del number_list[i]
        # reduce the list size
        n = n - 1
    else:
        # move to next item
        i = i + 1
print(number_list)
```

    [10, 20, 30, 40, 50, 60, 70]
    


```python

```
