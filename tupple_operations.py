"""
Tuple:
    1.Tuple is a immutable object
    2.Tuple object can be created by using parenthesis or by calling Tuple function
    3.Duplicates elements are  allowed
    4.Every element the tuple unique index
    5.List is change in the internal in the elements
    6.tuple is a static behaviour
    7.so list takes less memory
    8.a=()
     sys.getsizeof(a)
     its takes a one empty list 44 bytes
     after each elements takes 8 bytes
     but when we are append the list .then its takes each element  32 bytes

where(when) we use tuple: we d fixed the data we can go for tuple
                 when the internal references get change .
mutable:
       it's didn't chance the internal references

"""
'# slicing:'
import sys
l1 = (1, 2, 3, 4, 5, 6, 7)
print(l1)
print(len(l1))
print("===================")
print(l1[0])
print(l1[-100:-1])
print("===================")
'#print(dir(l1))'
"""
Tuple operations:
count():
      return the no.of items that is equal to given list
index:
      return the index of the first item that is equal to x
"""

t = 101, "Ravi", 12500, False
print (t)
count = t.count("Ravi")
print(count)
index = t.index(12500)
print(index)

"""
membership operators:
      we can test any item exist or not using membership operators
"""

print("Ravi" in t)
print("Ravi" not in t)
print("==============")
"""
delete:
       it will delete the complete element
"""
l2 = (1, 2)
print (l2)
del(l2)
'#delete the complete element '
