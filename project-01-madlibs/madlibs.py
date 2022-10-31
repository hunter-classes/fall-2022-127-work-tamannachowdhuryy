#2 extra imported files and name staying the same
import random
#this is my list of words that will then be implemented into my story 
HERO = ["Jack", "Carol", "Sam", "Tate", "Rally", "Carter", "Kat", "Flapie"]
VERB = ["little", "leave", "feel", "know", "see"]
NOUN = ["gold","piano","jelly","napkin" "flower"]
ANIMAL= ["bird", "fish", "cat", "tiger", "egale"]

#this is where my file is being opened by 
story = open('data2.txt')
data2 = story.read()

#to make it split
#words_from_data = data2.split()
lines_from_data = data2.split("\n")
story.close()

story = open("data2.txt","rt")
lines = story.readlines()
lines.append("This line has no newline")
stripped = []
for line in lines:
    stripped.append(line.strip())
story.close()
#will make two outputs and make sure the name will stay the same
loop = 1
while loop <= 2:
#this is for hero where ever the computer sees the word <HERO> it will be replaced with a random word from my list   
    def hero1(h):
      h = random.choice(h)
      hero_change = data2.replace("<HERO>", h)
      return hero_change
#this will make sure the change will happen in the story (data)
    change = hero1(HERO)  
#this is for verb we have to split verb again so we can connect the return for hero
    def verb(V):
      verb_change = change.split() 
      for repl_word in verb_change:
        if repl_word == '<VERB>':
          replacement = verb_change.index(repl_word)
          verb_change.pop(replacement) #we have to pop out <VERB> so we can replace it with a new one so we then use instert
          verb_change.insert(replacement, random.choice(V))
      return verb_change
    verb_change = verb(VERB)
#we contiune the same cycle to replace everything but this time for noun
    def noun(n):
      for repl_word in verb_change:
        if repl_word == '<NOUN>':
          replacement = verb_change.index(repl_word)
          verb_change.pop(replacement)#take out form dictionary
          verb_change.insert(replacement, random.choice(n)) #put in
      return verb_change
    animal_change = noun(NOUN)
   
    def animal(a):
      for repl_word in animal_change: #repl_word is the word that will be replaced when searched upon
        if repl_word == '<ANIMAL>':
          replacement = animal_change.index(repl_word)
          animal_change.pop(replacement) #take out form dictionary
          animal_change.insert(replacement, random.choice(a)) #put in
      finalStory = " ".join(animal_change) #inorder for the story to show we have to join the story togther by using empty quotes
      return finalStory #this then returns everything by going through the whole loop and replacing everything again
    finalStory = (animal(ANIMAL)) 

    print(animal(ANIMAL)) #finally prints the whole story 
    loop += 1
    