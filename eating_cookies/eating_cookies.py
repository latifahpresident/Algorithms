#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

#sys.argv is a list in Python, which contains the 
# command-line arguments passed to the script


how many ways can we get to n
n=5 cookies
1. 1 cookie 5 times 
2. 2 cookies then 3 cookies
3. 2 cookies one time then 1 cookie then 1 cookie then 1 cookie
4. 3 cookies one time then 1 cookie then 1 cookie


# 4 = 2 + 2
# 4 = 3 + 1
# 4 = 1 + 3
# 4 = 2 + 1 + 1
# 4 = 1 + 2 + 1
# 4 = 1 + 1 + 2 
# 4 = 1 + 1 + 1 + 1

def eating_cookies(n, cache=None):
  pass

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')