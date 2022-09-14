#For homework do the following:

#File folder: 9-15
#Filename: answers.py

#Do Ch 7 numbers 7,8,10, and 11

#7
def is_even(n):
    return n % 2 == 0

is_even(10) # True
is_even(5) # False
is_even(1) #False
is_even(0) #True
  
  
#8
def is_odd(n):
    return n % 2 > 0

is_odd(10) # False
is_odd(5) # True
is_odd(1) # True
is_odd(0) # False

#10
def is_rightangled(a, b, c):
    return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001

is_rightangled(1.5, 2.0, 2.5) #True
is_rightangled(4.0, 8.0, 16.0) #False
is_rightangled(4.1, 8.2, 9.1678787077) #True
is_rightangled(4.1, 8.2, 9.16787) #True
is_rightangled(4.1, 8.2, 9.168) #False
is_rightangled(0.5, 0.4, 0.64031) #True

#11
def is_rightangled(d, e, f):
    if d > e and d > f:
        return abs((e ** 2 + f ** 2) - (d ** 2)) < 0.001
    elif e > d and e > f:
        return abs((d ** 2 + f ** 2) - (e ** 2)) < 0.001
    else:
        return abs((d ** 2 + e ** 2) - (f ** 2)) < 0.001


is_rightangled(1.5, 2.0, 2.5) #True
is_rightangled(16.0, 4.0, 8.0) #False
is_rightangled(4.1, 9.1678787077, 8.2) #True
is_rightangled(9.16787, 4.1, 8.2) #True
is_rightangled(4.1, 8.2, 9.168) #False
is_rightangled(0.5, 0.64031, 0.4) #True

#Do Coding Bat, Stirngs_1 "hello_name, make_out_word, and first_two.

#hello_name
def hello_name(Bob):
    return "Hello " + Bob + "!";
#make_out_word
def make_out_word(out, word):
    return out[:2] + word + out[2:]
#first_two
def first_two(str):
    return str[:2]
