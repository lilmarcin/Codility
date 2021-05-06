def solution(N):
    result = 0
    if N > 0:
        i = 1
        factors = []
        while i <= N:
            if N % i == 0:
                factors.append(i)
            i += 1
        result = len(factors)
        print(factors)
    return result

if __name__ == "__main__":
    A = 22
    solution(A)