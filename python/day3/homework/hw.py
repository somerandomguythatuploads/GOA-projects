#first task
#-----------------------------------------------------------------------------------------------



#to create a variable we need to first assign a value to it.
#for example lets assign it a string. a string is a line of text wich is then displayed on a screen, a float is for example whatever this thing is 3.013, and a variable is a full number for example 2; 1; 11 and so on. now lets get back to the topic. the string is going to be "curcxela" and "i love".we are going to combine this to words with "+" and then print it.


a = "i love"
b = "curcxela"

print(a + b)

#as you can see it displayed "i love curcxela"



#second task:
#--------------------------------------------------------------------------------------------------


num1 = 10
num2 = 12
num3 = 125

print(num1 + num2 + num3)



#third task:
#---------------------------------------------------------------------------------------------------




x = 150
y = 2

print(x * y)



#fourth task:
#--------------------------------------------------------------------------------------------------



#for this task we want to make a rectangle and then calculate its diameter, the information:
#length = 20
#width = 10 
#the rectangles length is 20 and its width is 10 so to calculate its perimiter we will need to combine length(20) and width(10) and then multiply it 2 times bc a rectangle has two sides.
#ok so the formula will be: 2 * (20 +10)=60 so the perimiter equals to 30.

from turtle import *

color('yellow')
begin_fill()

forward(20)
left(90)
forward(10)
left(90)
forward(20)
left(90)
forward(10)

end_fill()


exitonclick()








#and here we go we have a 20*10 sized rectangle  i dont know how to zoom (i am writing a crying emoji)