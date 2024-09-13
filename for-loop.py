# loop
print("1")
print("2")
print("3")
print("4")
print("5")

for i in range(5):  # 0,1,2,3,4
    print(i)

for i in range(1, 6):
    # Here 1st parameter is index and last parameter is ending
    print(i)

for i in range(1, 6, 2):  # Here index[1] = start, index [6] = end and index[2] is skip
    print(i)  # odd

for i in range(0, 6, 2):  # even
    print(i)

#  1+2+3+4+5+...+100 =?
sum = 0

for i in range(1,101):    # i = 3
    sum += i    # sum = sum + i
    # sum = 3 + 3 = 6
print(sum)

# 1+3+5+...+100 = ?
for i in range(1,101,2):
    sum += i
    print(sum)

for i in range(0,101,2):
    sum += i
    print(sum)

for i in range(1,101) :
   if i % 2 == 0:
       continue
   else:
       sum = sum + i  #sum = 6

print(sum)

for i in range(1,101) :
   if i % 2 != 0:
    sum = sum + i

print(sum)

