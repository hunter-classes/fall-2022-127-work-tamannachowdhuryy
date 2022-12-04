#2 EXTRA (DAT file and translation in differnt language) 
f = open('input.txt','rt') #will open and read the txt file 
story = f.read() #will read the story 

pirate_file = open('pirate.dat', 'rt') #open the directory for my pirate data file 
english_dict = [] 
pirate_dict = []
#read the entire file
for word in pirate_file:
    #print(word)
    index = word.find(":") #will find the : in the pirate_file and seprate the string 
    left = word[0 : index : 1]
    english_dict.append(left)
    pirate_dict.append(word[index+1:len(word) - 1:1])

eng_words = story.split(' ')
#will change the words in the txt files
pirate_new_words = [] #empty lists to make a new list after change the txt file words 
redneck_new_words = []

#prints pirate sentence 

for word in eng_words:
    lastLetter = word[len(word) - 1 : len(word) : 1]
    if lastLetter != "!,." and lastLetter.isalpha() == False: #will ignore the puncutation 
        word = word[0: len(word) - 1: 1]
    if word in english_dict:
        pirate_new_words.append(pirate_dict[english_dict.index(word)])
    else:
        pirate_new_words.append(word)
pirate_new_text = ' '.join(pirate_new_words) #joins the stroy together but with the langauage changed 
print(pirate_new_text) # prints the whole story out 

#print redneck sentence
redneck_file = open('redneck.dat','rt')
redneck_dict = []
english_dict = []
for word in redneck_file:
    index = word.find(":")
    left = word[0 : index : 1]
    english_dict.append(left)
    redneck_dict.append(word[index+1:len(word) - 1:1])


redneck_new_words = []
for word in eng_words:
    lastLetter = word[len(word) - 1 : len(word) : 1]
    if lastLetter != "!" and lastLetter.isalpha() == False:
        word = word[0: len(word) - 1: 1]
    if word in english_dict:
        redneck_new_words.append(redneck_dict[english_dict.index(word)])
    else:
        redneck_new_words.append(word)

redneck_new_text = ' '.join(redneck_new_words) #join verything together
print(redneck_new_text)




