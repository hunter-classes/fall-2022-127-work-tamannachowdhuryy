import fizzbuzz

# this is a foreach loop 
for counter in range(1,101):
    if counter%3 == 0 and counter%5 != 0:
        print("fizz")
    if counter%5 == 0 and counter%3 != 0:
        print("buzz")
    if counter%3 != 0 and counter%5 != 0:
        print(counter)
    if counter%3 == 0 and counter%5 == 0:
        print("fizzbuzz")

counter = input("Put your number in: ")          