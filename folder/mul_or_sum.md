# Take 2 no. in input if the product of no's is greater than 500, then return their sum otherwise return their product only.


```python
def mul_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 500
    if product <= 500:
        return product
    else:
        # product is greater than 500 calculate sum
        return num1 + num2

num1 = int(input("Enter first number:-"))
num2 = int(input("Enter second number:-"))
result = mul_or_sum(num1, num2)
print("Result is :-",result) 
```

    Enter first number:-251
    Enter second number:-2
    Result is :- 253
    
