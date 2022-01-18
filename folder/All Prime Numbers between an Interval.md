```python
# Program to Print all Prime Numbers between an Interval.
x = int(input("Enter lower range: "))  
y = int(input("Enter upper range: "))  
      
for num in range(x,y + 1):  
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                break  
        else:  
            print(num)  
```

    Enter lower range: 8
    Enter upper range: 22
    11
    13
    17
    19
    


```python

```
