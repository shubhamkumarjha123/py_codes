# Removal of item from given list


```python
list1 = [5, 20, 15, 20, 25, 50, 15]#take list

import collections
print([item for item, count in collections.Counter(list1).items() if count > 1])#find only duplicate item and print them

list2 = list(dict.fromkeys(list1))#print each item once with help of unique dictionary value
print(list2)

def removeValue(sampleList, val):
   return [value for value in sampleList if value != val]
resList = removeValue(list1,50)#to remove specific value from list (like here we remove 50)
print(resList)
```

    [20, 15]
    [5, 20, 15, 25, 50]
    [5, 20, 15, 20, 25, 15]
    


```python
a = [11, 20, 15, 20, 25, 50, 20, 20, 11]
import collections
print([item for item, count in collections.Counter(a).items() if count > 1])

```

    [11, 20]
    


```python
list_ = ["a", "b", "a", "c", "c"]
list_ = list(dict.fromkeys(list_))
print(list_)
```

    ['a', 'b', 'c']
    
