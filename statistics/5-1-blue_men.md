[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```python
import scipy.stats
mu = 178
sigma = 7.7

# convert feet to cm
short = 5*30.48 + 10*2.54
tall = 6*30.48 + 1*2.54
# find normal cdf
s = scipy.stats.norm.cdf(short, loc=mu, scale=sigma)
t = scipy.stats.norm.cdf(tall, loc=mu, scale=sigma)
s, t, t-s
# about 34% of males are between 5'10" and 6'1"
```
```
(0.48963902786483265, 0.83238586549630633, 0.34274683763147368)
```

