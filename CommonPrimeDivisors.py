def prime(n):
    not_prime = set()
    primes = []
    if n == 1:
        primes.append(1)
    for i in range(2, n + 1):
        if i in not_prime:
            continue
        for f in range(i * 2, n + 1, i):
            not_prime.add(f)
        if n % i == 0:
            primes.append(i)
    return primes


def solution(A, B):
    count = 0
    for i in range(len(A)):
        print("Liczby:", A[i], B[i])
        primes_A = prime(A[i])
        primes_B = prime(B[i])
        primes_A = set(primes_A)
        primes_B = set(primes_B)
        print("Primes of A:" + str(primes_A))
        print("Primes of B:" + str(primes_B))

        if len(primes_A) == len(primes_B):
            if primes_A == primes_B:
                count += 1
    print("Liczba par z tymi samymi:",count)
    return count


if __name__ == "__main__":
    A = [1,6044400,3]
    B = [1,3022200,5]
    solution(A, B)