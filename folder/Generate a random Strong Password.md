# Generate a random Password which meets the following conditions.

 ##  Password length must be 10 characters long.
  ##  It must contain at least 2 upper case letters, 1 digit, and one special symbol.


```python
import random
import string

def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

print ("Password is ", randomPassword())
```

    Password is  6=XoiS{cDN
    


```python

```
