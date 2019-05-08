"""
#Code 1
my_list = [1,2,3]
your_list = ['a','b','c']

concat_list = my_list + your_list    # concat lists , operand unchanged
print(concat_list)


rep_list = my_list * 3      # replication , my list is unchanged

print(rep_list)


[1,2,3,4] < [1,2,3,0]       # first difference at index 3

[1,2,3,4] < [1,2,3,4,0]     # longer list is always greater


1 in my_list                # membership operation

1 in your_list


[1, 2,'one','two'] < [3, 4, 5, 6]     # no error , difference at 1 and 3

[1, 2,'one','two'] < [1, 2, 5, 6]     # error , comparison of 5 and 'o
"""


"""
Code 2
int_list = [1,2,3,4,5]
float_list = [1.0, 2.0, 3.0, 4.0, 5.0]
str_list = ['a', 'b', 'c', 'd', 'e']

nested_list = [int_list, float_list, str_list]

len(int_list)   #5
len(nested_list)    #3

min(float_list) #1

min(str_list)   #a
max(str_list)   #e

sum(int_list)   #
sum(str_list)     # elements must be numbers
"""


"""
#Code 3
my_list = [1, 2, 'a', 'z']
my_list[0]


my_list[0] = 'True'       # change the first element
print(my_list) 


my_list[-1] = 7           # change the last element
print(my_list)

my_list[:2] = [27]        # replace first two with 27
print(my_list)


my_list[:] = [1,2,3,4]    # change the whole list
print(my_list)


my_list[2:] = 'abc'       # change the last two elements
print(my_list)


my_list[:2] = 15          # only an iterable
print(my_list)            #can use an integer with an operator
"""


"""
#Code 4
a_list = [1, 12, 5, 8]
print(a_list)

a_list.append(17) 	        # append to the end
print(a_list)

a_list.append([40,50,60]) 	# append a list
print(a_list)

another_list = [20, 2]
a_list.extend(another_list)	# append each element to a list
print(a_list)

a_list.insert(3,'a') 	    # insert 'a' at position 3
print(a_list)

a_list.remove(8)
print(a_list)

a_list.pop() 		        # pop last element, return it
print(a_list)

a_list.index(17)	        # return index of argument

a_list.count(5)

a_list.reverse()            # reverse the list
print(a_list)

a_list.sort() 		        # sort the list
print(a_list)
"""

"""
#Code 5
result = 'this is a test'.split() 	           # split on whitespace
print(result)

result = 'field1,field2,field3,field4'.split(',')	# split on commas
print(result)


element1,element2,element3 = [1,2,3]		# multiple assignment from a list
print(element1)
print(element2)
print(element3)

field1,field2,field3 = 'Python is great'.split()   # multiple assignment from returned list
print(field1)
print(field2)
print(field3)


element1, element2 = [1, 2, 3] 	          # number of vars and elements on each side must match

element1, element2, element3 = [1, 2]
"""