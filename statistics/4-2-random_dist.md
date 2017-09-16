[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```python
ran = np.random.random(1000)
pmf = thinkstats2.Pmf(ran)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Config(xlabel='random num', ylabel='PMF')
```
![alt text]()

```python
cdf = thinkstats2.Cdf(ran)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='random num', ylabel='CDF')
```
![alt text]()

```
The random function is random because each number was selected with equal probability
```

