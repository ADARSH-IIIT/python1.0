

list1 = [  item  for item in range(5)     ]

print(list1)  
# [0, 1, 2, 3, 4]



list2 = [  item  for item in range(50) if item%2==0     ]

print(list2)  
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]




list3 = [  "adarsh"  , "dwivedi"  , "jai"   , "shree"  , "ram"  ]

list4 = [   item.upper()    for item in list3  ]
print(list4)
# ['ADARSH', 'DWIVEDI', 'JAI', 'SHREE', 'RAM']





list5 = ["hello"  for item in list3]
print(list5)
# ['hello', 'hello', 'hello', 'hello', 'hello']

# shortcut way to create a list 





# this is a way to create a new list from old 
# we can use this method as map function 