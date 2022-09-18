def piglatin(word):
    vowels = "aeiouAEIOU"
    con = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
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
word = input("Put your word in: ")
print(piglatin(word))