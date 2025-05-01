###2.2
```bash
    4000013 function calls in 1.233 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.233    1.233 C:\Users\Eugene Chan\Documents\schoolwork\CSCI3100_Software_Engineering\asgn_4_package\src\asgn_4_package\lib_raw.py:55(analyze)
        1    0.855    0.855    1.233    1.233 C:\Users\Eugene Chan\Documents\schoolwork\CSCI3100_Software_Engineering\asgn_4_package\src\asgn_4_package\lib_raw.py:1(longest_common_substr)    
  4000000    0.378    0.000    0.378    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 C:\Users\Eugene Chan\Documents\schoolwork\CSCI3100_Software_Engineering\asgn_4_package\src\asgn_4_package\lib_raw.py:34(longest_common_suffix)   
        1    0.000    0.000    0.000    0.000 C:\Users\Eugene Chan\Documents\schoolwork\CSCI3100_Software_Engineering\asgn_4_package\src\asgn_4_package\lib_raw.py:23(longest_common_prefix)   
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
```
###3.1 analyze
###3.2 longest_common_substr

###4.2 The change I've made is simple. I used a 2D array and dynamic programming. 
###4.3
```bash
------------------------------------------------------------------------------------------------ benchmark: 2 tests ------------------------------------------------------------------------------------------------
Name (time in ms)                                      Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS         
   Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_longest_common_substr_raw (NOW)              256.4865 (1.0)      262.0862 (1.0)      258.5826 (1.0)      2.5834 (1.0)      256.9721 (1.0)      4.2876 (1.0)           1;0  3.8672 (1.0)   
        5           1
test_longest_common_substr_raw (0001_38f08a9)     734.0980 (2.86)     742.5644 (2.83)     738.4698 (2.86)     3.2026 (1.24)     738.5854 (2.87)     4.5168 (1.05)          2;0  1.3542 (0.35)  
        5           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
===================================================================================== 7 passed in 4.37s ====================================================================================== 
```
