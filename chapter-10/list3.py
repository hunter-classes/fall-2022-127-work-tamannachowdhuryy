#5
def max(lst):
    max = 0
    for num in lst:
        if num > max:
            max = num
    return max
#7
import random 
def countOdd(lst):
    # your code here
    odd = 0
    for num in lst:
        if num % 2 != 0:
            odd = odd +1
    return odd
# make a random list to test the function
lst = []
for i in range(150):
    lst.append(random.randint(0, 1000))

print(countOdd(lst))
#8
def sumEven(lst):
    # your code here
    even = 0
    for num in lst:
        if num % 2 == 0:
            even += num 
    return even