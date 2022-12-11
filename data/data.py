#1 extra made a graph
#used pandas to compare data
from matplotlib import pyplot as plt
import pandas as pd
import csv
#average weight for heros using cvs file
weight = []
with open("heroes_information.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        weight.append(float(row["Weight"]))
print("Average weight:", sum(weight)/ len(weight))

#average height for heros using cvs file
height = []
with open("heroes_information.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        height.append(float(row["Height"]))
print("Average height:", sum(height)/ len(height))

#average of heros weight and height using cvs file
height = []
weight = []
with open("heroes_information.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        height.append(float(row["Height"]))
        weight.append(float(row["Weight"]))
print("Average height & wieght:", sum(height) / sum(weight))

#using pandas to find intersting data 
print('-------------------------------------------------------------------------')
#the median of heros weight for all genders 
df = pd.read_csv("heroes_information.csv")
median = df['Weight'].median()
print("Median hero weight:" + str(median))

#the median of heros height for all genders 
median = df['Height'].median()
print("Median hero height:" + str(median))

#Average length of word in the column Publisher
word = df['Publisher'].str.len().mean() #print out the length of words and the average length of words
print('Lengeth of word in Publisher:' + str(word))

print('---------------------------------------------------------------------')

#start of the graphs 
hero = pd.read_csv('heroes_information.csv')
#bar for gender and height
plt.bar(hero.Height, hero.Gender)
plt.bar(hero.Weight, hero.Gender)
plt.title("Heros Has the Same Weight & Height")
plt.xlabel("Height & Weight")
plt.ylabel("Gender")
plt.legend(['Height', 'Weight'])
plt.show()


#eye and race color scattered plot
plt.scatter(hero.EyeColor, hero.Race)
plt.title("Heros Has The Same Eye Color & Race")
plt.xlabel("Eye Color")
plt.ylabel("Race")
plt.show()
