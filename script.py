#!/bin/python3

#Variables and Methods

quote = "All is fair in love and war."
print(quote.upper())  #uppercase
print(quote.lower())  #lowercase
print(quote.title())  #title case

print(len(quote)) #count the length


name = "Health" #string
age = 30 #integer int(30)
gpa = 3.7 #float means number with decimal float(3.7)


print(int(age))
print(int(30.1)) #does not round


print("My name is " + name + " and I am " + str(age) + " years old.") #age must be a string to combine with other string

age +=1  #stored whats in the variable
print(age)

birthday = 1
age += birthday
print(age)


print('\n')



#FUNCTIONS
print("Here is an example function: ")

def who_am_i(): #this is a function
	name = "Heath"
	age = 30
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()


#adding parameters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)	


#multiple parameters
def add(x,y):
	print(x + y)

add(7,7)
	

def multiply(x,y):
	return x * y
	
print(multiply(7,7))
	

def square_root(x):
	print(x ** .5)

square_root(64)


def nl():
	print('\n')

nl() #new line



#BOOLEAN EXPRESSIONS (true or false)
print("Boolean Expressions: ")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9 

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))




#Relational and Boolean Operations
	
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7	

test_and = (7 > 5) and (5 < 7) #true
test_and2 = (7 > 5) and (5 > 7) #false
test_or = (7 > 5 ) or (5 < 7 ) #true
test_or2 = (7 > 5 ) or (5 > 7 ) #true

test_not = not True #false

nl()


#CONDITIONAL STATEMENTS

def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"

print(drink(3))
print(drink(1))


def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >=21) and (money < 5):
		return "Come back with more money"
	elif (age < 21) and (money >=5):
		return "Nice try, kid!"
	else:
		return "You're too poor and too young"
		
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))

nl()



#LISTS - have brackets
#count starts from zero

movies = ["Starwars", "The Hangover", "Harry Potter", "Gladiator"]

print(movies[1]) #return second item
print(movies[0]) #return first item
print(movies[1:3]) #starts from 1 and stops before item 3
print(movies[1:4]) 
print(movies[1:]) #starts from 1 up to the last entry
print(movies[:2]) #grabs everything before 3
print(movies[-1]) #grabs the last

print(len(movies)) #count
movies.append("JAWS")
print(movies)

movies.pop() #delete the last item on the list
print(movies)


movies.pop(0) #remove first item on the list
print(movies)

nl()



#TUples - like a list but do not change, () - list have brackets

grades = ("a", "b", "c", "d", "f")
print(grades[1])

nl()


#LOOPING

#FOR Loops - start to finish of an iterate

vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)
	
	
#WHILE loops - execute as long as true

i = 1

while i < 10:
	print(i)
	i += 1	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	








