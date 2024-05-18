"""

used to store multiple values of diff datatyprs in one name(in one var name)
then we use set listtuple and dict



list are changeable , can have same value multiple times  , ordered ===> 0 based indexing

"""




######################## how to create a list 

list1 = [ "val1" , 45 , "val3"  , True , 89.98  , 8+9j]

# using square brackets we can create list 


list2 = list(   ( "val1" , 45 , "val3"  , True , 89.98  , 8+9j , "val3")   )

# by using list constructor function , we can create list 
# but always use (()) double brackets 



print(type(list1))             #=====>>>> <class 'list'>




#################################  accessing list elements 

print(   list2[3]  )

# as we access eleemnts in array 


# we can also do indexing 

print(  list1[2:5]  )   # 2nd 3rd and 4th element








##################         CHECKING EXISTANCE OF ANY SPECIFIC ITEM IN LIST  #######################


if "val3" in list1 :
    print("yes , it exist")
else :
    print("no it does not exist")    



###############################    iterating in list ###################################

for item in list1:
    print(item)    




#########################################################    manipulating elements of list ###########



l = ['one' , 'two' , 'three' , 'four' , 'five']
print(id(l))

l[0]= 'five'
print(id(l))

# both id are are same , means no new list is created , same list has been modifies


b= l 

# b is also ointing to l 
# b koi new list nahi hai
b[2] ="new two"

# l[2] , bhi change ho gaya hoga 

# b and l both are pointing to same memory address 


##########################################################################################################



l1 = ['one' , 'two' , 'three' , 'four' , 'five']
l2 = l1


print(   id(l1)  , id(l2)  )

# both are pointing to same memory address

l3 = list(l1)

print(   id(l1) , id(l2) , id(l3)   )    #140100176874560 140100176874560 140100176877312

# l3 is totally new list , copy of l1 


##########------------------------------------------------------------------------------------------------------------








#---------------------------------   changing  a range of elements of list at a time ------------------


l1 = ['one' , 'two' , 'three' , 'four' , 'five']


print(l1)
l1[2:5] = [   "new three" , "new four" , 'new five'       ]


print(l1)










# ======================================================    APPEND INSERT EXTEND method =====================




list1 = ["one" , 'two'  , 'three']

list1.append("adarsh")

print(list1)   # it will add adarsh in the same list at the end , no new memeory is allocated to new list , memeory address remain same




#  error , reason ======>>>>>>  append , can take only one argument at a time , can add one item at a time at the end of list
# list1.append(1 ,"adarsh")

# print(list1) 




#######   insert 
# it will insert new single item at specific index 

list1.insert(1 , "orange")
print(list1)

#it will add orange at 1st index and shift all list by one place



# =========================================================
# list1.insert(3 , "orange" , 4 , "mango")
# print(list1)

# error only take 2 argu , 1st is for index number , second is for new value to be added 




############### extend function 

# this fun will take only one argument   ,  any iterable object 

list1.extend(   ["new1" , "new2" , "new3"]   )
print(list1)

# add these val at the end of list 

# we can pass tuple set anything , bas ek iterable object hona chahiye


# list1.extend( "a" , "b"   , "c" )
# print(list1)

### errorrrrrrrrrr


list1.extend( ( "a" , "b"   , "c" ))
print(list1)

# no error as we are passing tuple as argument

















# ==========================================    removing items from list 


# list ke jitne bhi method hote hai , sare same list ko modify krte hain , means no new memory address pe ek new list nahi create hoti hai 

list1 = ["one" , 'two'  , 'three']


print(list1.remove("two"))

# "two will be removed" , but two ko return nahi karega 

print(list1.pop(0))  ### elemet of zero index will be popped out , and list1[0] ko return bhi karega

#### by default , pop() , last element ko pop karega 



list1.clear()
print(list1)
## it empties the list , but list completly delelte nahi hogi======> []






# ******************************* vimp ********************************************************

"""del list1
print(list1)

  print(list1)
NameError: name 'list1' is not defined. Did you mean: 'list2'?

"""
# ******************************* vimp ********************************************************






################################   adding two list          ################################################


l1 = ["first list"]
l2 = [" second list"]


l3 = l1 + l2


# new l3 list has been created 


l2.extend(l1)

# l2 has been extended 
#############################################################################################################






#####   using list methods we can find index of elements in list , sort , reverse the list and so many things , study acc to use 