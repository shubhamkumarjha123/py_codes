# Generate  random String of length 5


```python
import random
import string

def randomString(stringLength):
    """Generate a random string of 5 charcters"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
print ("Random String is ", randomString(5) )
```

    Random String is  iALkf
    


```python

```
