# list: collection of items that are unordered changeable and indexed
# tuple: collection of items that are ordered , unchangeable
# set: collection of items that are unordered ,unchangeable/unindexed
# list in python


variablename =[ 'item1' , 'item2','item3']
shoppingList = ['toothpaste', 'cake', 'tissuepaper']

# accessing items in a list
item0 = shoppingList[0]
print(item0)

# item0 =shoppinglist
item2 =shoppingList[2]
print(item2)

# list slicing
print(shoppingList[1:2])
print(type(shoppingList))
print(type('hello'))
print(type(2))
print(type(2.1))

# changing values in a list
# variablename(index)-new item
shoppingList[0] = 'book'
print(shoppingList)


# # List length
# append(): adds an item in a list at the end of the list
# insert():adds a specific index
# pop() :removes the last item in a list
# del :deletes the whole list
# clear: removes items in a list/returns an empty list
# extends: adds more than one item in a list

shoppingList.append("tooth paste")
print(shoppingList)
shoppingList.insert(1,'milk')
print(shoppingList)
shoppingList.pop()
print(shoppingList)

# del shoppingList[3]
print(shoppingList)

# del shoppingList
print(shoppingList)

# ASS:research on clear and extend
# checking if an item exists in list
if 'cakes' in shoppingList:
    print('Cake is present in the list')
else:
    print('cakes is not the list')
if 'cakes'  in shoppingList:print('cake is present in the list')


# Pyhton Dictionary Datastructure
# a dic comes in pairs
# a dic is made up of key and a value
john={
    "height": 5.7,
    "counrty":"Kenya",
    "language":['Pyhton',"Java","javascript"]
}
print(type(john))
print(john)

# accessing keys and values
# syntax :accessing values
# dictvariable[key]
john["height"]
print(john["height"])

print("language")
# syntax:accessing values
# dictname.get(key)
john.get("country")


# changing dictionary value
# syntax:dictname['key']="new value"
john['country']="Egypt"
print(john)

# looping through a dict;allows you to interact with
key_list =[]
value_list =[]
for data in john:
    key_list.append(data)
value_list.append(john[data])
print(key_list)
print(value_list)
    #print(data + ":"+ str(john[data]))

# loooping thru value_list
for val in john.values():print(val)
# looping thru both keys and values
for my_key,my_value in john.items():
 print("KEY" + my_key +"VALUE" +str(my_value))


 # adding keys and values to an existing dict
 #  # syntax:dictname[newkey] =new value_list
 john['status']= 'complication'
 john['occupation']='Python Eng'
 print(john)


 # ass;remove keys and values in a dict
 # deleting a dict
 # clearing a dict
 # coping a dict

# creating a tuple
profile =("john","male",1999)
profile =(("john","male",1999))
print(profile[0])


shoppingList =list()
john2=dict()
# profile2 =tuple()

# sets;unordered and unindexed
fruits ={"apple","banana","pine"}
for fruit in fruits:
    print(fruit)

    # adding item in sets...use add method
fruits.add("mango")
fruits.add("avocado")

    # adding items ;;use update method
fruits.update("cherry","berry")
# ass: deleting a tuple...you use del

...#  getting the size of a set..print(len(thisset))
# testset..testdict

# if statements,for,while loop,function
del fruits