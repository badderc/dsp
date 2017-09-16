# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequences of items, but lists are mutable and tuples are immutable. Because lists can be changed after assignment, they cannot be used are keys in dictionaries. Tuples, however, can be used as keys because they are constant and cannot be changed after they are assigned. Both can be assigned as values in dictionaries though.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are sequences like lists, but they contain only unique items and their ordering is arbitrary. Sets are useful for checking for the existance of an item (check x in set). Sets would be faster for finding an element because each item is unique. Lists are more useful for iterating through a sequence.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's 'lamdba' function is an anonymous function that is used when you need to perform a relatively simple operation for a short period of time and don't really need to define a named function. They are often used as arguments in other built-in functions to quickly evaluate and return values within the larger function. In 'sorted', 'lambda' can be part of the 'key' argument: a = [[1,2], [4,5], [6,0]] and then to sort this list of lists by the second item in each list: b = sorted(a, key=lambda x: x[1]). 

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are an easy way to make patterned lists without using a for loop because the expression can be simply stated inside the brackets. They can be used in place of map and filter operations. Set comprehensions are functionally very similar to list comprehensions but they eliminate the occasional issue of repeated values and are constructed with curly brackets instead of square. Dictionary comprehensions act similarly, but the expression applies to the values and depends on the keys.

```python
# list comp
items = [1, 2, 3, 4, 5]
i_sqrd = [x**2 for x in items]
>> [1, 4, 9, 16, 25]
# same list using map (function, sequence)
i_sqrd = map(lambda x: x**2, items)
>> [1, 4, 9, 16, 25]

# list comp
letters = ['a', 'B', 'c', 'D', 'e', 'F']
l_up = [up for up in letters if up.isupper()]
>> ['B', 'D', 'F']
# same list using filter (function, sequence)
l_up = filter(lambda up: up.isupper(), letters)
>> ['B', 'D', 'F']

# set comp
items = [2, 4, 6, 8]
s = set(x/2 for x in items)
>> set([2, 3, 1, 4])
# dictionary comp
words = ['hi', 'hi', 'hello', 'hey', 'hello', 'sup', 'howdy', 'hello']
d = dict((k, words.count(k)) for k in words)
>> {'howdy': 1, 'hi': 2, 'hello': 3, 'sup': 1, 'hey': 1}

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>>  937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





