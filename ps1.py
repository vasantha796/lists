# list1 = [1,2,3,4,3,2,5,6,7,8]
# u = []
# d = []
# for i in list1:
#     if list1.count(i) > 1 and i not in d :
#         d.append(i)
#     elif list1.count(i) == 1 :
#         u.append(i)
# print(u)
# print(d)  
# 
# l = [1,2,3,4,6,5,6,5,7] reverse this 

# check if array is subset of a list
# arr1 = [1,3,4,5,2]
# arr2 = [2,4,3,1,7,5,15]
# print(set(arr1).issubset(set(arr2))) #method 1 

# arr1 = [1,3,4,5,2]
# arr2 = [2,4,3,1,7,5,15]
# c = 0
# for i in arr1:
#     if i in arr2:
#         c += 1
# if c == len(arr1):
#     print("subset")
# else:
#     print("not a subset")          

# l = [1,3,4,5,2]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i] > l[j]:
#             l[i],l[j] = l[j],l[i]
            
# print(l)   swapping 
# print('max',l[0])
# print('min'l[-1])


# arr1 = [202,89,112,88] #sum of digits
# for i in arr1:
#     s = 0
#     l1 = []
#     while i > 0:
#         r = i %10
#         s += r 
#         i = i // 10
#     l1.append(s)
    
# print(l1)    
# 
# ascii values : ord 
# print(ord('a')) character to value 
# print(chr(65))  value to character 

# for i in range(ord('a'),ord('z')+1):
#     print(i) prints all the ascii values

# for i in range(ord('a'),ord('z')+1):
#     c = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             c += 1
#     if c == 2:
# #         print(chr(i))        

# a = 10
# b = 20
# a,b = 0,1
# while a <= 20 :
#     if a >= 10:
#        for i in range(2,a):
#            if a % i == 0:
#                break
       
#            print(a)
#     a,b = b,a+b    

# nums = [2,7,11,15]
# target = 9
# n = len(nums)
# for i in range(n):
#     for j in range(i+1,n):
#         if nums[i] + nums[j] == target:
#             print([i,j])


                 


        

        
    











