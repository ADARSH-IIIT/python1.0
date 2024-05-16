


"""

two types 
implicit
explicit

"""



##############################    explicit    ###############   type conversion by us

x = "2"

y = int(x)

"""
newvar= int(oldvar)
newvar= float(oldvar)
newvar= str (oldvar)

"""

# python interpreter tries to convert , but it may give error also


# eg

x = "adarsh"

print(   int(x)     )

# Traceback (most recent call last):
#   File "/home/adarsh/Desktop/python/_8_typecasting.py", line 34, in <module>
#     print(   int(x)     )
# ValueError: invalid literal for int() with base 10: 'adarsh'


####################################################################################





############################################    implicit conversion   ############################

# done by interpreter itself to avoid data loss 

x = 10

y = x + 5.6

print(type(y))

# as datatype of y is float , python select datatype of more size to avoid data loss