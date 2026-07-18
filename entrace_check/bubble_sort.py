# bubble sort algorithm in Python 
print("Enter a list of numbers (Space separated):")
lst = list(map(int, input().split()))

n = len(lst)
for i in range(n-1):
  for j in range(n-i-1):
    if lst[j] > lst[j+1]:
      lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst) 