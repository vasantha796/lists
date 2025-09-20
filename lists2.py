# edge cases # code quality  # role of inbuilt function
# whn the question is strght forward no to inbuilt function

# 1.print 6th index: 1st approach

# def find_element(input_list,input_index):
#     return input_list[input_index]

# l = [1,2,3,4,5,-32,-45,9]
# index = int(input("enter yr index :"))
# print(find_element(l,index))

#when the index given isnt in the list (edge case):
# def find_element(input_list,input_index):
#     if input_index < -len(input_list) or input_index >= len(input_list):
#         return "invalid index"
# l = [1,2,3,4,5,-32,-45,9]
# index = int(input("enter yr index :"))
# print(find_element(l,index))

# sum,max,min

# l = [1,2,3,4,5,-32,-45,9]
# l.sort()
# print(l[-1]) #method 1 
# if the list is mt

# def max_element(input_list):
#     if len(input_list) == 0:
#         return "empty list"
    
#     input_list.sort()
#     return input_list[-1]

# l = [1,2,3,4,5,-32,-45,9]
# print(max_element(l))


# most efficient way of prntng max num

# l = [1,2,3,4,5,-32,-45,9]
# max_element = l[0]
# for i  in l :
#     if i > max_element:
#         max_element = i
# print(max_element)  


#  minimum 
# l = [1,2,3,4,5,-32,-45,9]
# min_elem = l[-1]

# for i in l:
#     if i < min_elem:
#         min_elem = i
# print(min_elem)        

# we can wrte all the 3 under the same roof:

# l = [1,2,3,4,5,-32,-45,9]
# sum = 0 
# min_elem = l[0]
# max_elem = l[0]
# for i in l:
#     sum += i

#     # to fin max
#     if i > max_elem:
#         max_elem = i

#     # to fin min 
#     if i < min_elem :
#         min_elem = i
# print(sum,max_elem,min_elem)

# avg of numbers in the list : sum of nums/len of digits

# rev  a list :
# l = [1,2,3,4,5,-32,-45,9]
# l.reverse()
# print(l) method 1

# slicing : while using this method you shud also re-assign
# l = [1,2,3,4,5,-32,-45,9]
# l = l[: : -1]
# print(l) method 2

# 
# l = [1,2,3,4,5,-32,-45,9]
# new_list = []
# for i in l :
#     new_list.append(i)

# print(new_list) prints same list 

# l = [1,2,3,4,5,-32,-45,9]
# new_list = []
# for i in l:
#     new_list.insert(0, i) # adds each new elem in 0th index

# l = new_list
# print(new_list)


# l = [10,20,50,-32,67]
# for ind in range(0,len(l)-1, -1, -1):
#     print(ind)
#     print(l[ind])

# print all the num in even index :
# l = [1,2,3,4,5,-32,-45,9]
# for i in range(0,len(l),2):
#     print(l[i])
# based on values in list use for i in list 1
# based on index go for range

# efficient method : two pointer approach as we take low and high or 2 points
# l = [1,2,3,4,5,-32,-45,9]
# low = 0
# high = len(l)-1
# while low < high :
# #     l[low],l[high] = l[high],l[low]
# #     low += 1
# #     high -= 1

# # print(l)    

# # rev a str two pointer approach doesnt work on  str why ?
# # sum of digits in a particular num of a list [123,44,521] = [6,8,8]

# # sorting
# # bubble sort & linear search

# list1 = [10,-3,700,45,23,100,-300]
# for i in range(0, len(list1)- 1):
#     if list1[i] > list1[i+1]:
#         list1[i],list1[i+1] = list1[i+1],list1[i]

#     print(list1)
# 6 iterations are enough 






 







