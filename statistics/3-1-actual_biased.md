[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> ```python
import chap01soln
import thinkstats2
import thinkplot
>>
resp = chap01soln.ReadFemResp()
>>
pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
>>
def BiasPmf(pmf, label=''):
    new_pmf = pmf.Copy(label=label)
>>
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
>>        
    new_pmf.Normalize()
    return new_pmf
>>
biased_pmf = BiasPmf(pmf, label='observed')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='children', ylabel='pmf')
>>
print pmf.Mean()
print biased_pmf.Mean()
```
Actual mean: 1.02420515504  
Biased mean: 2.40367910066
