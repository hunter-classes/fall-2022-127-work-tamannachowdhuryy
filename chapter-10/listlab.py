#Write a function to find the smallest value in a listKfind smallest in a list of items
list = [2,3,4,-1,-4,-5]
def listKfind(list):
    min = list [0]
    for a in list:
        if a < min:
            min = a
    return min

print(listKfind(list))

#Write a function that returns a new list that contains
#all the odd items in the original list
list = [1,2,5,7,6,10]
def countOdd(list):
    # your code here
    odd = 0
    for num in list:
        if num % 2 != 0:
            odd = odd +1
    return odd
print(countOdd(list))



#Write a function that takes a string and returns a new string where
#all the words are capitalized.
def capitalize(string):
    vowels = "aeiouAEIOU"
    con = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
string = "this should be uppercase!"
print(string.upper())
        
        
#Write a function that takes a string and returns a new string with
#every word that's longer than 5 character turned into upper case
def capitalize(string):
    vowels = "aeiouAEIOU"
    con = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# example string
string = "playboys!"
print(string.swapcase())
        #comeback to this 


#Write a function that takes a list of numbers and returns a new list
#with each item squared
import math
result = [math.sqrt(i) for i in [2,4,6,8]]
print(result)
   

#Write a function that takes two lists of numbers and returns a new
#list where each item is the corresponding values of the original
#lists added together. Ex [1,2,3] and [10,20,30] would return the
#list [11,22,33]


test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]
  
# printing original lists
print ("Original list 1 : " + str(test_list1))
print ("Original list 2 : " + str(test_list2))
  
# using naive method to 
# add two list 
res_list = []
for i in range(0, len(test_list1)):
    res_list.append(test_list1[i] + test_list2[i])
  
# printing resultant list 
print ("Resultant list is : " + str(res_list))
    

#chapter 10
#10
def length_5(a_list):
    """Returns how many words in a list have length equal to 5."""
    words_of_five = 0
    for i in a_list:
        if len(i) == 5:
            words_of_five += 1
        else:
            words_of_five += 0
    return words_of_five


print(length_5(["hello", "mom", "party", "cheese", "chocolate"]))

#11
import random

def sum(lst):
    sum = 0
    index = 0
    while index < len(lst) and lst[index] % 2 != 0:
        sum = sum + lst[index]
        index = index + 1
    return sum

lst = []
for i in range(100):
    lst.append(random.randint(0,1000))

print(sum(lst))

#12
lst = ["able", "been", "state", "Sam", "beer"]
length = len(lst)
def test(lst):
    length = len(lst)
for w in lst:
    if w == "Sam":
        break
    print(w)
print(test(lst))
