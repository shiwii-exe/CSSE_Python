string=input("Enter the string: ")
print(string)

freq = {}
for char in string:
 if  char in freq:
  freq[char] += 1
 else:
  freq[char] = 1
res = max(freq, key = freq.get)

print ("The maximum frequency in the given string is : " + str(res))