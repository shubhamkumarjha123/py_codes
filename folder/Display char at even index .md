# For a string, display char that present at even index. 


```python
def EveIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print("index[",i,"]", str[i] )

inputStr = str(input("enter char"))
print("Orginal String is ", inputStr)

print("Print even index chars")
printEveIndexChar(inputStr)
```

    enter charhelloworld
    Orginal String is  helloworld
    Printing only even index chars
    index[ 0 ] h
    index[ 2 ] l
    index[ 4 ] o
    index[ 6 ] o
    index[ 8 ] l
    
