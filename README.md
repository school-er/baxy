# Baxy
Baxy Python Division System

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


# What Is This?
I've always had a fascination about computers doing division and failing at it. So, I decided to build my own division program.
We have our own custom adding decimal system, and Baxy can do problems that python usually can't

# How do I implement it into my project?
Use import baxy (or from baxy import divide), and do baxy.divide(*number to divide*, *number to divide by*) or baxy.divide('*number to divide*/*number to divide by*') as either work.

# What are some bugs in Baxy?
There is one bug that is persistent that we're working on fixing, that sometimes there's a multiplication error that happens due to Python

(e.g. 11.2 * 0.1 = 1.1199999999999999)

In version 2 of Baxy, we're gonna try to implement our own custom multiplication system to combat this

# What do the error codes mean?

Common error codes:
NOT_VALID_EQUATION - You didn't put in a valid division equation in properly

DIVIDE_BY_ZERO - You divided by zero

L1TO, L2TO - It took longer than 10 seconds to do an equation, most likely a multiplication error happened

If however you get L3TO, I'd like to see what the equation was, so please submit it to the email below

GTR10 - The rarest error code, If you got this please submit it to contactcrampy@gmail.com


If however you get an error that is not listed here, and with a valid equation, please submit it.

# What is an example implementation?

```python
    from baxy import divide
    print('Enter number to divide')
    num1 = input('>')
    print('Enter number to divide by')
    num2 = input('>')
    print(divide(num1, num2))
```
