# Write a function called exponent(base,exp) that returns an integer value of base raise to the power of exp.

```python
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)
```

    5 raises to the power of 4 is:  625
    


```python

```
