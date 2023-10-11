def counter(a,b):
    for i in range(b):
        a += 2*i
    return a

data = int(input())
x = 0
c = counter(x, data)
print(c)