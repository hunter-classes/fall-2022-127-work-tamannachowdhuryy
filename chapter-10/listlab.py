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
list = [1,2,5,7,6,10]
def countOdd(list):
    # your code here
    odd = 0
    for num in list:
        if num % 2 != 0:
            odd = odd +1
    return odd
#all the odd items in the original list

#Write a function that takes a string and returns a new string where
#all the words are capitalized.

#Write a function that takes a string and returns a new string with
#every word that's longer than 5 character turned into upper case

#Write a function that takes a list of numbers and returns a new list
#with each item squared

#Write a function that takes two lists of numbers and returns a new
#list where each item is the corresponding values of the original
#lists added together. Ex [1,2,3] and [10,20,30] would return the
#list [11,22,33]

#chapter 10 # 10, 11, 12