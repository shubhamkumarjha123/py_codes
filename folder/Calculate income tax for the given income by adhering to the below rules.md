# Calculate income tax for the given income by adhering to the below rules.


```python
income = 45000
taxPayable = 0
print("Given income", income)

if income <= 10000:
    taxPayable = 0
elif income <= 20000:
    taxPayable = (income - 10000) * 10 / 100
else:
    # first 10,000
    taxPayable = 0

    # next 10,000
    taxPayable = 10000 * 10 / 100

    # remaining
    taxPayable += (income - 20000) * 20 / 100

print("Total tax to pay is", taxPayable)
```

    Given income 20000
    Total tax to pay is 1000.0
    


```python

```
