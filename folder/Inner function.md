# Make a inner funct.


```python
def manipulate(x, y):
    # concatenate two strings together
    def inner_fun(x, y):
        return x + y

    z = inner_fun(x, y)
    return z + 'Shubham'

result = manipulate('My', 'Name-')
print(result)
```

    MyName-Shubham
    
