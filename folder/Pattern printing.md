# Print pattern


111111111                                                                   
22222222                                                                                                        
3333333                                                                                              
444444                                                                                                       
55555               
6666                                                                            
777                                                                                 
88                                                                           
9                           


```python
row = 9
y = 0
# reversing loop i.e 9 to 0
for i in range(row, 0, -1):
    y += 1
    for j in range(1, i + 1):
        print(y, end=' ')
    print('\r')
```

    1 1 1 1 1 1 1 1 1 
    2 2 2 2 2 2 2 2 
    3 3 3 3 3 3 3 
    4 4 4 4 4 4 
    5 5 5 5 5 
    6 6 6 6 
    7 7 7 
    8 8 
    9 



```python

```
