start = 0
end = 999

print("Prime numbers between 0 and 999 are: ")

for num in range(start, end + 1):

   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)