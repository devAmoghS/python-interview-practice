# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def q3(start, end):
  res = []
  for i in range(start, end+1):
    if i%7 == 0 and i%5 != 0:
      res.append(i)
  return res

result = q3(2000, 3200)
print(result)
