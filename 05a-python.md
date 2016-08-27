# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are mutable meaning they can be altered in-place without creating a new object in memory. You cannot change a tuple in-place, only create a new one. Only tuples will work as dictionary keys because the keys must be hashable and only immutable objects can be hashed.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are unordered and cannot contain duplicate elements. They are mutable like lists (but frozensets are immutable). You can do operations like union, intersection, and difference with sets. Sets can be searched through in constant time rather than linear time due to hashing optimizations, but will take more memory space. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is used to create an anonymous function in just one line.  
```python
lst = [('Bob', 3), ('Alice', 2), ('Carl', 1)]
sorted(lst, key = lambda x: x[1])  # Returns [('Carl', 1), ('Alice', 2), ('Bob', 3)]
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions create or alter a list based on some rules. The use of map/filter/reduce vs. list comprehension is a widely debated issue in the world of Python. There is no drastic speed difference so either works fine, it's up to personal preference to choose whichever makes the code clearer.  
```python
# Map comprehension
map(str, [1,2,3])
[str(i) for i in [1,2,3]]
# Filter comprehension
filter(lambda x: type(x) == str, [1,2,'a'])
[x for x in [1,2,'a'] if type(x) == str]
# Set comprehension
{i for i in [1,1,2,2,3]}  # Returns {1,2,3}
# Dict comprehension
{k:v for k,v in [('A',1), ('B',2), ('C',3)]}  # Returns {'A': 1, 'B': 2, 'C': 3}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```python
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





