
"""
function has 2 parts definiiton and calling 

"""





# ========================================================= ==========================================================
def fun1():
    print("hello world this is first function")

fun1()    
# ========================================================= ==========================================================









# ========================================================= ==========================================================
def fun1(   arg  ):
    print("hello world this is first function" , arg)

# fun1(  )    
#error as we have not passed arg in function calling



# fun1("adarsh") 
#no error 
# ========================================================= ==========================================================







# ========================================================= ==========================================================
""""
types of arguments

def fun(  a , b )  =====>    a and b both are necessary argu , we have to pass them uring fun call
def fun(  a= "some default value"  , b )  =====>    a is not necessary as it has some default val , but b is  necessary argu , we have to pass b during fun call



def fun (  all non default para  , default para )
eg 

def fun(arg1 = 55  , arg2)====> wrong fun definition
def fun(arg2  ,  arg1 = 55 ) ===> correct fun definition


"""


"""

how to call fun

def fun(a , b)

fun(50 , 60)=======> a=50 and b=60 ho jayega

fun(b=89 , a=90)  is tarah bhi call kr sakte hain

"""

# ========================================================= ==========================================================








# ==============================  advanceway to write and call functions ====================


def fun1(   *list_of_arg   ):
    print(list_of_arg)
    print(type(list_of_arg))  #===========> it is sored in fornm of tuple , so that we can not change it


fun1(12 , 56,"asfas" , 67)




def fun1(   **list_of_arg   ):
    print(list_of_arg)
    print(type(list_of_arg))  #===========> it is sored in fornm of dict , key val pair


fun1(a= 7 , b= 90 )

# if we use ** , the nwe have to pass argu in form of a=90 , b=87 , c="aad" , so that it is easy to make dict







"""

we can pass list tup set dict directly as param in function

"""



def changer(listl):
    sum=0
    for item in listl:
        sum = sum+ item

    return sum    
        

print(    changer(    [1,3,2,4,5]      )    )



#similarly with set , tup , dict  etc 












# ========================================    vvvimp ==============================================



# pass 

# if we dont want to write function definition right now , then we can use pass statement


def funname(args):
    pass






a=b=6 
if a<b :
    pass

# pass can be used at different places 