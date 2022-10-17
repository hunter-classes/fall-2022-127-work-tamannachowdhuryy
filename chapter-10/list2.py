#4
def average(numlist):
    # Complete the function definition
    total = 0
    for num in numlist:
        total = total + num

    return total / len(numlist)
#tries
#tries average
toy = [90, 25, 30]
print("toy:", toy)
average=(toy)
print("Average:",average)

#6

list = [2,3,4]
def sum_of_squares(xs):
    sumSquares = 0
    for num in xs:
        sumSquares += num ** 2
    return sumSquares

print(sum_of_squares(list))
