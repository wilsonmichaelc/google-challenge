#!/usr/bin/python

import string

#names = ["annie", "bonnie", "liz"]
#names = ["abcdefg", "vi"]
#names = ["al", "cj"]
#names = ["annie", "bonnie", "liz", "al", "cj", "zyz"]
#names = ["annie", "al", "zys", "bonnie", "liz", "cj"]
#names = ["annie", "bonnie", "cj", "liz", "al"]

def​ ​wordValue(name):
​ ​​ ​​ ​​ ​v=0
​ ​​ ​​ ​​ ​for​ ​l​ ​in​ ​name:
​ ​​ ​​ ​​ ​​ ​​ ​​ ​​ ​v​ ​+=​ ​string.ascii_lowercase.index(l)+1
​ ​​ ​​ ​​ ​return​ ​v
​ ​​ ​​ ​​ ​
def​ ​answer(names):
​ ​​ ​​ ​​ ​#​ ​your​ ​code​ ​here
​ ​​ ​​ ​​ ​names.sort(reverse=True)
​ ​​ ​​ ​​ ​names.sort(key=lambda​ ​x:​ ​wordValue(x),​ ​reverse=True)
​ ​​ ​​ ​​ ​return​ ​names
