# random password generating program

from random import random, sample

alpha = ['A','B','C','D','E','F','G','H','I','J',\
'K','L','M','N','O','P','Q','R','S','T','U','V','W',\
'X','Y','Z','a','b','c','d','e','f','g','h','i','j',\
'k','l','m','n','o','p','q','r','s','t','u','v','w',\
'x','y','z','0','1','2','3','4','5','6','7','8','9']

nums = sample(range(len(alpha)),8)

print(nums)

c1 = nums[0]
c2 = nums[1]
c3 = nums[2]
c4 = nums[3]
c5 = nums[4]
c6 = nums[5]
c7 = nums[6]
c8 = nums[7]

print(sample(alpha,8))