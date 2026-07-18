# define fibinnaci series in recursive form
def fib(x):
    if x<=0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

# print the first 10 numbers in the fibonacci series
for i in range(10):
    print(fib(i))