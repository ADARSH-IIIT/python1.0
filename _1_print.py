print("hello world")



x = 10
print(x)                             #=================>>>>>   print======> println




print("str 1" , "str 2"  , )





########################  vimp

print(   "str1"   ,  "str2"  , "str3"   ,    sep = " seperator string here "  )
# str1 seperator string here str2 seperator string here str3
# space will be added by default

# print("hello world" , "bye world"  ,  end=" this will append at the last of the string (bye world) ")
# hello world bye world this will append at the last of the string (bye world)







###################################################################################################
# there is problem
# if we use end , then print does not behave as println

print("line 1"  , end=" ender statement")
print("line 2")
print("line3")

# final output
# line 1 ender statementline 2
# line3





#################################################################################################################
print("line 1"  , end=" ender statement\n")
print("line 2")
print("line3")

# final output
# line 1 ender statement
# line 2
# line3







#####################################################################################################
print("dfdfdfdf"  , end=None)
print("gjggj")

# here none will act as \n