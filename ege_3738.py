def sum_digits(n):
    sum_d = 0
    for i in str(n):
        sum_d += int(i)
    return sum_d


with open('17_3738.txt') as f:
    A = [int(i) for i in f]
B = []
for i in range(1, len(A) - 1):
    if sum_digits(A[i - 1]) == sum_digits(A[i + 1]):
        B.append(sum_digits(A[i]))
print(len(B), max(B, key=lambda x: B.count(x)))





