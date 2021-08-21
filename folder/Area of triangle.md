# Area of triangle


```python
x = float(input('first side:'))
y = float(input('second side:'))
z = float(input('third side:'))

# Calculating semi-perimeter .
s = (x + y + z) / 2
# Area formula
area = (s*(s-x)*(s-y)*(s-z)) ** 0.5
print('Area of triangle %0.1f' %area)
```

    first side:6
    second side:7
    third side:8
    Area of triangle 20.33
    
