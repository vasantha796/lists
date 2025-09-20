# set bilt-in methods wid examples
# add()= adds an element to a set
# s={1,2,3}
# s.add(5)
# print(s) #{1,2,3,5}

# remove()= removes an element 
# s={1,2,3}
# s.remove(2)
# print(s) #{1,3}

# error: keyerror is raised if element is not found.
# s={1,2,3,4}
# s.remove(5)
# print(s) raised element not found

# discard()= functions just like remove and it doesnt pass any error if element is not found.
# s={1,2,3,4}
# s.discard(6)
# print(s) # {1,2,3,4}

# pop()=it pops out elements on a random case
# s={1,2,3,4,5}
# print(s.pop()) # 1
# print(s) #{2,3,4,5}

# # clear()=removes all elements at once 
# s={1,2,3,4,5,7}
# s.clear()
# print(s) #set()

# copy() return a shallow copy
# s={1,2,3,4}
# c=s.copy()
# print(c)#{1,2,3,4}

# union:returns all the unique elements from both sets
# a={1,2,34,56,78}
# b={2,3,4,567,890}
# print(a.union(b))

# update():updates the set with union of another set
# a={1,3,4,56}
# a.update({3,45,56})
# print(a)

# intersection():returns common elements
# a={1,3,4,5,6}
# b={2,3,45,67}
# print(a.intersection(b))

# difference(): returns elements in first set bt nt in second()
# a={1,2,3,4,5}
# b={1,3,456,7}
# print(a.difference(b))

# difference_update(): removes elements of another set
# a={1,3,5,6,78}
# b={3,4,56}
# a.difference_update(b)
# print(a)

# symmetric_difference(): returns elements in either set but not both.
# a={1,2,34,45}
# b={3,5,6,7}
# print(a.symmetric_difference(b))

# symmetric_difference_update(): updates set wid symmetric difference
# a={1,2,3,}
# b={3,4,5}
# (a.symmetric_difference_update(b))
# print(a)

# issubset():checks if all elements of one set exists in another
# a={1,3}
# v={1,2,3}
# print(a.issubset(v))

# issuperset(): checks if set contains all elemnts of another
# a={1,3,5}
# b={1,3}
# print(a.issuperset(b))

# isdisjoint(): returns true if 2 sets have elemnts in common
# a={1,2}
# b=(3,4)
# print(a.isdisjoint(b))



# ###frozen set
# as frozen set is immutable only copy(),union()
# intersection(),dffrence(),
# symmetric_diffrence(),issubset(),issuperset(),isdisjoint()  possible
#
# methods like add(),remove(),clear() 
# 


