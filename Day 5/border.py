M = int(input("Enter number of rows (M): "))
N = int(input("Enter number of columns (N): "))
print("Enter matrix elements:")
matrix = [list(map(int, input().split())) for _ in range(M)]

border_sum = 0
for r in range(M):
    for c in range(N):
        if r == 0 or r == M - 1 or c == 0 or c == N - 1:
            border_sum += matrix[r][c]
            
print(f"Border sum: {border_sum}")