N = int(input())

R = 3
for i in range(N):
    result = R**2
    R += R-1
print(result)