# To reverse the word.


```python
def rev(Sentence):
    
    words = Sentence.split(" ")
    
    # iterate  the list and reverse each word using ::-1
    new_word_list = [word[::-1] for word in words]
    
    # to jpin the new list of words
    res_str = " ".join(new_word_list)
    return res_str
str1 = "My Name is shubham "
print(rev(str1))
```

    yM emaN si mahbuhs
    


```python

```
