# Fibonacci sequence printing in python


```python
no_of_terms = int(input ("No of terms you want to print \t"))  
     
# First two terms  
a = 0  
b = 1  
count = 0  
      
#check if the number of terms is valid or not  
if no_of_terms <= 0:  
    print ("Accepts only positive integer")  
# if there is only one term, it will return n_1  
elif no_of_terms == 1:
    print ("The Fibonacci sequence of the numbers up to", no_of_terms, ": ")  
    print(a)  
# Then we will generate Fibonacci sequence of number  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < no_of_terms:  
        print(a)  
        nth = a + b  
        # At last, we will update values  
        a = b  
        b = nth  
        count += 1  
```

    No of terms you want to print 	9
    The fibonacci sequence of the numbers is:
    0
    1
    1
    2
    3
    5
    8
    13
    21
    


```python

```
