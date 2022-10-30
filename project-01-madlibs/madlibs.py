#2 EXTRAS

from random import shuffle
#EXTRA 1 make a file     
f = open("data2.txt")
file_content = f.read()


words_from_data = file_content.split()
lines_from_data = file_content.split("\n")
f.close()

f = open("data2.txt","rt")
lines = f.readlines()
# we can strip out the newlines from
# lines

# adding a line without a newline
# just to show
lines.append("This line has no newline")
stripped = []
for line in lines:
    stripped.append(line.strip())
f.close()
       
#variables list
NOUN = ["gold","piano","jelly","napkin" "flower"]
ANIMEL= ["bird", "fish", "cat", "tiger", "egale"]
VERB = ["little", "leave", "feel", "know", "see"]
PLACE = ["new york", "heaven", "classroom", "portal"]
COLOR = ["red", "yellow", "orange", "green", "blue", "purple", "white", "black"]
HERO = ["Jack", "Carol", "Sam", "Tate"]
ADJECTIVE = ["aggressive", "arrogant", "dizzy","calm"]
    
     
# NOUN initializing replace word for noun
repl_word = "<NOUN>"
# shuffing list order
shuffle(NOUN)
for ele in NOUN:
     
    # replacing with random string
    file_content = file_content.replace(repl_word,ele)
    
# VERB initializing replace word 
repl_word = "<VERB>"
# shuffing list order
shuffle(VERB)
for ele in VERB:
     
    # replacing with random string
    file_content = file_content.replace(repl_word,ele)
    
# PLACE initializing replace word 
repl_word = "<PLACE>"
# shuffing list order
shuffle(PLACE)
for ele in PLACE:
     
    # replacing with random string
    file_content = file_content.replace(repl_word,ele)
    
# VERB initializing replace word 
repl_word = "<COLOR>"
# shuffing list order
shuffle(COLOR)
for ele in COLOR:
     
    # replacing with random string
    file_content = file_content.replace(repl_word,ele)
#EXTRA 2 make sure name stays the same through the story     
    # VERB initializing replace word 
repl_word = "<HERO>"
# shuffing list order
shuffle(HERO)
for ele in HERO:
     
    # replacing with random string
    file_content = file_content.replace(repl_word,ele)
    
repl_word = "<ADJECTIVE>"
# shuffing list order
shuffle(ADJECTIVE)
for ele in ADJECTIVE:
     
    # replacing with random string
    file_content = file_content.replace(repl_word,ele)

repl_word = "<ANIMEL>"
# shuffing list order
shuffle(ANIMEL)
for ele in ANIMEL:
     
    # replacing with random string
    file_content = file_content.replace(repl_word,ele)
#prints the whole doc out
print(file_content)