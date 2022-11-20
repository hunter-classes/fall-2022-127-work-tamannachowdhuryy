def piglatin(word):
    vowels = "aeiouAEIOU"
    con = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    pun = ".!?"
    leftCon= ""
    rightCon= ""
    
    if word[0] in con:
        leftCon= word[0] + "ay"
        for i in range(1,len(word)):
            rightCon += word[i]
        rightCon += leftCon
    elif word[0] in vowels:
        leftCon= word[0] + "yay"
        for i in range(1,len(word)):
            rightCon += word[i]
        rightCon += leftCon
    return rightCon
    if word[-1] in ".!?":
        end_of_sent = True
        pun = word[-1]
        word = word[:-1]
    else:
        end_of_sent = False
        
# Testing
test_word = "hello"
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "play"
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "Sad"
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "Able"
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "Mad."
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "made."
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "Cranky!"
result = piglatin(test_word)
print(test_word," -> ",result)

test_word = "deBug!"
result = piglatin(test_word)
print(test_word," -> ",result)
