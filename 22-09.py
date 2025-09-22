# def sock_days(socks):
#     sock_counts = {}
#     for color in socks :
#         if color in sock_counts:
#             sock_counts[color] += 1
#         else:
#             sock_counts[color] = 1


#     total_pairs = 0
#     for count in sock_counts.values():
#         total_pairs += count //2

#     return total_pairs    
# socks = ['red', 'green', 'red', 'purple', 'green', 'black', 'red']
# print(sock_days(socks)) #2 

# 2. Find the missing numbers. Input: 34571  	Output : 26 missing

# 3.Matrix addition using range.

n1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

n2 = [[9,8,7],
      [6,5,4],
      [3,2,1]]
rows = len(n1)
cols = len(n1[0])
c = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(n1[i][j] + n2[i][j])
    c.append(row)
for row in c:
    print(row)        
      



                           