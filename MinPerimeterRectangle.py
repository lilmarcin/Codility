import math
def solution(N):
    result = []
    if N <= 0:
        return 0
    for i in range(int(math.sqrt(N)), 0, -1):
        if N % i == 0:
            print("a:",N/i, "b:",i)
            result.append(2 * (i + N / i))
    print(min(result))

if __name__ == "__main__":
    A = 30
    solution(A)