2.2
```bash
        5007865 function calls in 0.937 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.937    0.937 C:\Users\Eugene Chan\Documents\schoolwork\CSCI3100_Software_Engineering\asgn_4_package\src\asgn_4_package\lib_raw.py:81(analyze)
        1    0.605    0.605    0.936    0.936 C:\Users\Eugene Chan\Documents\schoolwork\CSCI3100_Software_Engineering\asgn_4_package\src\asgn_4_package\lib_raw.py:1(longest_common_substr)
  4006002    0.234    0.000    0.234    0.000 {method 'append' of 'list' objects}
  1001850    0.097    0.000    0.097    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 C:\Users\Eugene Chan\Documents\schoolwork\CSCI3100_Software_Engineering\asgn_4_package\src\asgn_4_package\lib_raw.py:60(longest_common_suffix)
        1    0.000    0.000    0.000    0.000 C:\Users\Eugene Chan\Documents\schoolwork\CSCI3100_Software_Engineering\asgn_4_package\src\asgn_4_package\lib_raw.py:49(longest_common_prefix)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
```
3.1 analyze
3.2 longest_common_substr

4.2 The change I've made is simple. I used a 2D array and dynamic programming. 
4.3
```bash
------------------------------------------------------------------------------------------------ benchmark: 2 tests ------------------------------------------------------------------------------------------------
Name (time in ms)                                      Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_longest_common_substr_raw (NOW)              257.5656 (1.0)      262.1546 (1.0)      258.9583 (1.0)      1.9892 (2.16)     257.8044 (1.0)      2.6950 (1.64)          1;0  3.8616 (1.0)           5           1
test_longest_common_substr_raw (0001_6d1e2e1)     325.5556 (1.26)     327.6053 (1.25)     326.6400 (1.26)     0.9225 (1.0)      326.3524 (1.27)     1.6402 (1.0)           3;0  3.0615 (0.79)          5           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 7 passed in 4.32s ============================================================================ 
```
