[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```python
resp = nsfg.ReadFemResp()

pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')

biased_pmf = BiasPmf(pmf, label='observed')

print('Actual Mean: ', pmf.Mean())
print('Observed Mean: ', biased_pmf.Mean())
```
```
Actual Mean:  1.02420515504
Observed Mean:  2.40367910066
```
```python
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Config(xlabel='Children per HH', ylabel='PMF')
```
