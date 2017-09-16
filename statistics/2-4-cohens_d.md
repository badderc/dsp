[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
```python
d = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print(d)
# because the effect is negative, the firsts are technically lighter than the others, but it is a very small diff
firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean()
# looking at the means, firsts are a little lighter than others
```
``` 
-0.0886729270726
(7.201094430437772, 7.325855614973262)
```

```python
diff = abs(CohenEffectSize(firsts.prglngth, others.prglngth)) - abs(CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb))
print(diff)
# The total weight has a slightly larger effect size than the pregrancy length when comparing firsts and others
```
```
-0.0597938824182
```
