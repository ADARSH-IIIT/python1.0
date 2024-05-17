# ==
# <=
# >=
# !=
# <
# >

# these all return true or false 


print(5>6)   # false 



if True:
    print("execute this statement")

elif True :
    print("execute this")

else :
    print("execute this")





# elif ======> else if 


a = 200
b = 300


if a>b :
    print("1")

elif a==b:
    print("2")

elif a<b :
    print("3")

else :
    print('4')        






"""

if a>b:
print("sdsd")


indentation error
 print("fdf")    
    ^
IndentationError: expected an indented block after 'if' statement on line 63

"""    



# ------------------------------------    if else new shortcut syntax   -------------------------------

if a>b : print("hello")

elif a<b : print("bye")

else : print("jai ho")

# --------------------------------------------------------------------------------------------------------




print ("hello") if a>b  else print("bye")

print ("hello") if a>b       else  print("ramm raam") if a<b       else print("bye")
# |--- block 1 ----------|   |    block 2                   |      |     block3    |








# we can also use and or not with these condn 

x = 4 
y = 5


if not a==b:
    print("a and b are unequal")


if  a!=b:
    print("a and b are unequal")    


# both are doing same thing 





