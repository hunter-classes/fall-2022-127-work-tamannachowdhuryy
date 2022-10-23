import math
#my list of numbers
l = [2,6,8,34,56,23,56,45,45,2,3,6,56]
#findLargest(l) which takes in a list of numbers and returns
#the value of the smallest number
def findLargest(l):
    min = l[0]
    for a in l:
#a has to be less then the min other words the random number 
        if a < min:
            min = a
    return min
print(l)
print(findLargest(l))
#freq(l,v) which takes a list of numbers (l) and a value (v).
#The function will return the freuqeency
#of v, that is, the number of times that v appears in l.
l = [2,6,8,34,45,23,45,45,45,2,3,6,56]
v = 45
def freq(l,v):
    count = 0
#if the number is equal to 1 count 1 and then return it to the count    
    for i in l:
        if i == v: count += 1
    return count
print(l)
print(freq(l,v))
