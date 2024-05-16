
#####################################################################    


                        #  memeory address of var 
variable = "Hello, World!"
address = id(variable)
print(f"The memory address of the variable is: {address}")
# /////////////////////////////////////////////////////////////////////



x = 5
y = "John"
print(x)
print(y)








x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)





x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 




# ////////////////////////////////////////////////////////
x = 5
y = "John"
print(type(x))
print(type(y)) 
# <class 'int'>
# <class 'str'>
# ////////////////////////////////////////////////////////////






# //////////////////////////////////////////////    vimp/////////////////////
x = 'john'
y="john"

print(x==y) #==============>>>   true

# 'str'  is same as "str"









a= 4
A = 40

# both are different var








##################################################   asignment of multiple values 

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


################################################## 


x = y = z = "Orange"
print(x)
print(y)
print(z)









################################################    destructuring of list

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)








#######################################   confusions #################


x = 4+5     #valid

y = "str1" +'str2'

z = 4 + "fdfdfdf"     #   error , we cant concat str and number


newvar = str(4) + "dfdfdf"    #  ok , as 4 is now string 




x = str(4)

y = int('4')    # ok

z = int("adarsh")   # error , as we cant conert adarsh to any number 

print(y)