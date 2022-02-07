# Wap to Check the type of an obj.


```python
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class van(Vehicle):
    pass

School_van = van("School Eeco", 12, 50)

# Python's built-in type()
print(type(School_van))
```

    <class '__main__.van'>
    


```python

```
