# 1.conditional statements
# looping

# a.if ..checks ifa single condition is true
# b.if ..else executes the condition that is not true
# c.if..elif ...else executes the condition the conditions before it,if they are not true
#
#     If statements most of the time make use of the assignment operators ie;< ,>,<= ,>= ,!=

x = 5
y = 3
if x < y: #checks for true conditions
    print(str(x) +"greater than" +str(y))
    print("{} is greater {}".format(x,y))
elif x < 10:
    print("{} is greater {}".format(x,10))
else:#checks for false conditions
    print("{} is not less than {}".format(x, y))

    # nested if
if x > y:
    if y > 4:
        print("y is greater than 2, but less than {}".format(x))
    else:
        print("y is not greater than {} and {}".format(2,x))
else:
    print("{} is not greater than {}".format(x,y))

    #
    # LOOPING
    # While loops :

count = 0
while count < 10:
     print("Hello world")
     count = count + 1
num = 0
while num <=10:
     print(num)
     num = num + 1

# break and continue statements
num2 = 0
while num2 <=10:
    if num2 ==5:
        print("at the middle")
    break
    print(num2)
    num2 = num2 + 1

num3=0
while num3 <= 10:

    if num3 == 5:
        print("at the middle")
        break
    print(num3)
    num3 = num3 + 1


    # for loops
for letter in "John":
    print(letter)

for i in range (5): #i is an interger..numbers
        print(i)
for i in range(3,10,2):
            print(i)
            # range (starting point, ending point,increament value)

for i in range(10):
    print(i)
else:
    pass

# write a program that printd the smallest and the largerst number i in the list
# numbers=[210, 0,34,65,33,54,54,54,3,65]
#
# django framework
# classes