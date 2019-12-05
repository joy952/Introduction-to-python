# Pyhton Function:
# 1.a block of code with a name
# 2.this function only works when in use
# 3.helps us to write repeated code

def nameOfFunction():#creating a function
    print('Hello world')

nameOfFunction()#calling a fuction in python

# naming a function:
# # # 1. should start witha lower case
# # # 2.should start with a letter or an underscore

def greeting_1(name):
    print("Hello world" + name)
def greeting_2(name, country,gender ):#takes more than one argument
    print("My name "+name + "I come from" +country + "I am" + gender)

greeting_1("John")
greeting_2("John","Kenya","Male")

# default parameter
def greeting_3(name="Developer"):#takes one arg
    print("Hello world" + name)

greeting_3()
greeting_3("Mary")


def sum_of_two_num(number_1,number_2):
    print(number_1 +number_2)
sum_of_two_num(3,5)


def sumOfTwoNum(number_1, number_2):
      theSum=(number_1 + number_2)
      return theSum

ans = sumOfTwoNum(5,6)
print(ans)







# ass:create a function that computes an area of a circle of a given radius

def area_of_a_circle(PIE ,radius):
    area=PIE *radius
    return area

ans=area_of_a_circle(3.14,7)
print(ans)

shoppingList =['Soap','sugar','bread','cooking oil',['spoon','pot'],{"name":"john"},
print(shoppingList[4][0]),
print(shoppingList[5])
loopList(theList)
loopList(shoppingList)

