N = int(input("Enter N: "))
matrix = [[0] * N for _ in range(N)]
for i in range(N):  
    if N % 2 != 0:
        matrix[i][i] = 1
    else:
        matrix[i][N - 1 - i] = 1

print("Resulting matrix:")
for row in matrix:
    print(*row)

