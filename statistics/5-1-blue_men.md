[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> ```python
import scipy.stats
>>
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
>>
low = dist.cdf(177.8)    # 5'10"
high = dist.cdf(185.4)   # 6'1"
>>
print high-low
```
>> 0.342094682946  
Around 34.2% of the U.S. male population is between 5'10 and 6'1 in height.
