# check if a number is even or odd
# def even_odd(n):
#     return "Even" if n % 2 == 0 else "Odd"
# n = int(input("enter yr num:"))
# print(even_odd(n))

# 2.find the max and min in a list 
# def max_min(arr):
#     max_arr = arr[0]
#     min_arr = arr[0]
#     for num in arr :
#         if num > max_arr :
#             max_arr = num
#         elif num < min_arr:
#             min_arr = num
#     return max_arr,min_arr
# arr = [10,30,20,40,50]
# print(max_min(arr))                      

# 3.reverse a strng widout using slicing 
# def string_rev(str1):
#     rev = ''
#     for i in str1:
#         rev =  i + rev 
#     return rev 
# print(string_rev('vasu'))    

# 4. check if a string is palindrome 
# def check_palindrome(str1):
#     for i in str1:
#         if str1 == str1[: : -1]:
#             return True 
#         else:
#             return 'Ala kaadh ra picchoda'
# print(check_palindrome('sir'))    
# print(check_palindrome('madam')) 

# 5. find the factorial of a number 

# def factorial(num):
#     fact = 1
#     for i in range(1,num +1):
#         fact*= i
#     return fact
# n = int(input("enter yr num :"))
# print(factorial(n))   
# 
#6. count freq of a character in a string 
# def count_freq(n):
#     str1 = {}
#     for ch in n :
#         if ch in str1:
#             str1[ch]+=1
#         else :
#             str1[ch] = 1
#     return str1
# print(count_freq('vasantha'))            

# 7. find the second largest number 
# def second_largest(arr):
#     arr.sort()
#     return arr[-2]
# print(second_largest([10,30,40,50]))

# 8.find how many vowels and consonants in a string 
# def vowels_consonants(s):
#     vowel_count = 0
#     cons_count = 0
#     vowels = 'aeiouAEIOU'
#     for ch in s:
#         if ch in vowels:
#             vowel_count+=1
#         elif ch not in vowels :
#             cons_count +=1

#     return vowel_count,cons_count
# print(vowels_consonants('ALLU ARJUN'))        

# 9. sum of digits of a number 
# def sum_of_digits(num):
#     sum = 0
#     while num > 0 :
#         digits = num % 10
#         sum += digits
#         num //= 10
#     return sum
# print(sum_of_digits(515502)) 
# 
# 10. print multiplication table 
# n = 5
# for i in range(1,11):
#     print(n,'x',i,'=',n*i)

# 11.find the longest word in a sentence\
# def longest_word(s):
#     longest = ''
#     words = s.split()
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest
# print(longest_word('naako gun esthaaraaa !!'))    
# 
# 12. removing duplicates from list

# def find_duplicates(arr):
#     seen = set()
#     dup = set()
#     for i in arr:
#         if i in seen :
#             dup.add(i)
#         else:
#             seen.add(i)  
#     return dup,seen
# print(find_duplicates([1,2,3,3,2,1,4,5])) 
# 
# 13.sorting a list 
# def sorting_list(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#         return arr
# print(sorting_list([2,5,2,6,9,1,8,4,2]))   

# 14.merge two list into a single sorted list
# n1 = [4,3,6,5,2]
# n2 = [1,7,8,9,0]
# n1.extend(n2)
# n1.sort()
# print(n1)

# 15.check if a number is prime or not 
# def check_prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             return "prime kaadh ra babu" 
#     return 'prime number'
# print(check_prime(6))     
# ---------------------------medium---------------------------------------
# 1.find all pairs in a list that sum upto target
# def twosum(arr,target):
#     n  = len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i] + arr[j] == target:
#              return [i,j]
            
# print(twosum([2,7,11,15],9))                                

# 2.rotate a number by k positions 
# def rotate_number(arr,k):
#     s = str(arr)
#     k %= len(s)
#     return int(s[-k:] +s[:-k])
# print(rotate_number(12345,2))

# 3.find the missing number in the consecutive numbers
# def find_missing(arr):
#     n = len(arr)+1
#     total = n * (n+1) // 2
#     return total - sum(arr)
# print(find_missing([1,2,4,5]))

# 4. check if two strings are anagrams 
# def anagrams(n1,n2):
#     return sorted(n1) == sorted(n2)
# print(anagrams('care','race'))

# 5.count the number of words in a sentence
# def count_words(sentence):
#     return len(sentence.split())
# print(count_words("crying is only coming!!!"))

# 6.remove all duplicates from a sentence
# def remove_dup(statement):
#     words = statement.split()
#     res = []
#     for i in words:
#         if  i not in res :
#             res.append(i)
#     return ''.join(res)  
# print(remove_dup('emundhile inka padko padko '))      

# 7.invert a dictonary (keys to values)

# def invert_dict(d):
#     return {v: k for k, v in d.items()}

# print(invert_dict({'a': 1, 'b': 2, 'c': 3}))

# 8.find the intersection of two lists
# def intersection(lst1,lst2):
#     return list(set(lst1) & set(lst2))

# print(intersection([1,3,4,5,6],[3,5,7,9]))

# 9.print the transpose of a matrix

# 10.implement bubblesort
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
# print(bubble_sort([3,5,2,1]))   
# 
# 11. find the non repeating character in a string
# def non_repeating(c):
#     for i in c:
#        if c.count(i) == 1 :
#            return i 
#     return None 
# print(non_repeating('swiss'))

# 12.find the longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words,key = len)
print(longest_word("holidays ayipoinaiiiiiii"))

# 13.find the second smallest in list
# def second_largest(arr):
#     unique = sorted(set(arr))
#     return unique[1] if len(unique) > 1 else None
# print(second_largest([3,5,7,9,3,1]))

# 14.check if a number is armstrong number

def is_armstrong(n):
    temp = n
    digits = 0
    while temp > 0 :
        digits += 1 
        temp //= 10
    temp = n 
    total = 0
    while temp > 0 :
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return n == total 


print(is_armstrong(153))       
    
    








 

  





        