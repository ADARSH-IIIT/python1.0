


strvar = "this si a string"

x = 'this is also string'



a = "adarsh"
b= 'adarsh'


# both a and b are exactly same 

print(a==b)    #==============>>>>>>> true



####################################################################################


# printing quotes inside str 


print(   "     my name is  '''   adarsh      "           )


print(   '     my name is  """   adarsh      '          )


print(   "     my name is  \"   adarsh      "           )

print(   '     my name is  \'   adarsh      '           )





#############################################    MULTILINE STRING      //////////////////////////////

"""



strr =  " adadasd 
afdfdf
dfdfdfdfd
fdfdfdfd
fdfdfd
fdfdfdfdd"


####   this is error ###########


"""



# to solve this

strrr =   """
fgfgfg
fgfgfg
fgfgfgf
gfgfg

"""


# we can use triple single or double quote

########################################################################











# //////////////////////////////////    length of str 


a = "dfdfdfdfdf"


print (    len(a)          )





# //////////////////////////////////////  looping each char of string //////////////////

for i in "banana":
  print(i + " extra string optional hai")

'''
output
b extra string optional hai
a extra string optional hai
n extra string optional hai
a extra string optional hai
n extra string optional hai
a extra string optional hai
'''






# /////////////////////////////////////////////////////////     checking substr in string /////////////////////

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")



txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# ///////////////////////////////////////////////////////////////////////////////////////////////////







txt = "The best things in life are free!"
varr = "free"  in txt
print(varr)   #############++++++++>>>>>   return true or false



txt = "The best things in life are free!"
print("expensive" not in txt)

# ////////////////////////////////////////////////////////////////////////////////