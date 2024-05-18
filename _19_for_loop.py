"""

for loop is used in

string
range
list , tuple set etc

used in any iterable object of python 




syntax




for iterator in object :
        do these things , till end of iterable object


"""





# ====================================================   examples 



str = "banana"

for i in str :
    print(i)


"""
b
a
n
a
n
a
"""
# iterator will always points to item inside object  
#we can use break continue if else etc things inside foor loop as other programming lang



""""

str = "banana"

for i not in str :
    print(i)



ERROR DEGA ===>   not in is not valid     

"""




# ===============================================


# range 


"""

range is an object that can have atmax 3 argument and atleast 1 argument


range(a,b,c)
range(a,b)
range(a)


it returns an iterable object 


eg 


range(5) return iterable obj from 0 to 5-1==4    0 to 4

range(10) return iterable obj from 0 to 9


range(  5  ,  120) return iterable obj from 5 to 119



range(  5  ,  20  ,  3) return iterable obj from 5 ,  5+3 , 8+3 , 11+3 , 14+3 , 17+3 
20 will be neglected 5 to 19 with step of 3 


range(5 , 2)   , empty obj 

agar koi non feasible condn dale toh empty obj return hoga , jiske upar hum iterate nahi kar payege






for i in range('a' , 'c'):
    print(i)


error    , range ke andar sirf integer ho sakte hain , and wo sirf integer ka obj return krta hai    
"""





# =================================  best way to understand range ===================


x = range( 5 , 120 , 4)


print(   list(x)   )

# it will print all items inside range



# ================================================================  loop with list tuple etc 


l = [ "first" , "second" , "third" , "fourth"  , "fifth" ]


for item in l :
    print(item)



# nested eg 


for item in l :

    for char in item:
        print(char , end='   ')
    
    print()




# if we want we can directly pass list as obj 
for i in [23,45,67]:
    print(i)
# ============================================================


tup = ( "first" , "second" , "third" , "fourth"  , "fifth" )

for item in tup :
    print(item)



# same syntax for set dict etc 
# study in upcoming files 