"""
List:
    1.List is a mutable object
    2.list object can be created by using square brackets or by calling list function
    3.Duplicates elements are allowed
    4.Every element the list unique index
    5.List is change in the internal in the elements
    6.List is a dynamic behaviour
    7.so list takes more memory
    8.a=[]
     sys.getsizeof(a)
     its takes a one empty list 64 bytes
     after each elements takes 8 bytes
     but when we are append the list .then its takes each element  32 bytes

where(when) we use list: we did not fixed the data we can go for list
                 when the internal references get change .the we don't change the
                 main references  then we go for list
mutable:
       it's chance the internal references

"""
import sys
a = [1, 2, 3, 4, 5, 6, 7]
print(a)
sys.getsizeof(a)

'#============================'

"""
1.append(): 
         add the element end of the list
         append() takes exactly one argument
         once we give two or more  elements this time its came type error 
"""
a.append(2)
a.append([2, 3, 4])
print(a)
"""
1.a.append([2, 3, 4],2)
a.append([2, 3, 4],2)
TypeError: append() takes exactly one argument (2 given)
"""

'#============================'

""" 
2.extend():
          Add all elements of a list to the another list

#1.what is the difference between append and extend
sol:
    append returns the element end of the list and extend also same 
    *but extend add the elements other list
    * append also it's take other list in list in argument position 
    * but extend add the elements in list sequence type.like one element by element
    
"""
b = [7, 8, 9]
a.extend(b)
print(a)
'#============================'
"""
3.insert():
         insert() - Insert an item at the defined index
         insert() Parameters
The insert() function takes two parameters:

index - position where an element needs to be inserted
element - this is the element to be inserted in the list

"""


b.insert(3, 0)
'#inserting: time using two arguments (first argument(3) takes index value)'
'#: second argument(0), what ever we change the element'
print("this inserting:", b)

print('================================')
"""
4.remove() - Removes an item from the list
The remove() method searches for the given element in the list and removes the first matching element
remove() Parameters
The remove() method takes a single element as an argument and removes it from the list.

If the element(argument) passed to the remove() method doesn't exist, valueError exception is thrown.

Return Value from remove()
The remove() method only removes the given element from the list. It doesn't return any value.
once is there more duplicate values it's remove first duplicate element

"""
Remove = ["Ramesh", "Suresh", "siva"]
Remove.remove("siva")
print("remove:siva", Remove)
print('=================================')

"""
count:count() - Returns the count of number of items passed as an argument
"""
vowels = ["a", "e", "i", "o", "u"]
count = vowels.count("i")
print("count of vowels:", count)
print('==================================')

"""
pop():
     The pop() method removes the item at the given index from the list. 
     The method also returns the removed item.
     

"""
# programming language list
language = ['Python', 'Java', 'C++', 'French', 'C']

# Return value from pop()
# When 3 is passed
return_value = language.pop(3)
print('Return Value: ', return_value)

# Updated List
print('Updated List: ', language)
print('=================================')
"""
reverse():
        The reverse() method reverses the elements of a given list.
  """
# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# List Reverse
os.reverse()

# updated list
print('Updated List:', os)
print("================================")

"""
sort():
       sort() - Sort items in a list in ascending order
"""

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)
print("=====================================")

"""
copy:
     sort() - Sort items in a list in ascending order
"""
old_list = [1, 2, 3]
new_list = old_list

# add element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)
print("======================================")

"""
index() - Returns the index of the first matched item
"""
itr = [1, 2, 3, 4, 56]
for i in itr:
    print(i)
