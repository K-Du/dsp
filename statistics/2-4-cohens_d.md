[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> ```python
import nsfg 
>>
preg = nsfg.ReadFemPreg()
>>
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / pooled_var**0.5
    return d
>>
live = preg[preg.outcome == 1]
>>
firsts = live[live.birthord == 1].totalwgt_lb
others = live[live.birthord != 1].totalwgt_lb
>>
print CohenEffectSize(firsts, others)
```

Cohen's D for birth weight is -0.08867, which is low just like the value for pregnancy length (0.029). This means the difference in means is only 0.08867 standard deviations, thus we can assume there is not a significant difference between the groups.
 
 
