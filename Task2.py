def todec(n):
    wynik_n = suma_n = 0
    for i in range(0, len(n)):
        wynik_n = n[i] * (-2) ** i
        suma_n = wynik_n + suma_n
    return suma_n


def suma(A, B):
    liczba = []
    if len(A) < len(B):
        while len(A) < len(B):
            A.append(0)
    else:
        while len(A) > len(B):
            B.append(0)
    C = [A[j] + B[j] for j in range(len(A))]
    print(C)
    for i in range(0, len(C)):
        if C[i] == 0:
            liczba.append(0)
        elif C[i] == 1:
            liczba.append(1)
        elif C[i] >= 2 and C[i] % 2 == 0:
            liczba.append(0)
            if i+2 < len(C):
                C[i+1] += int(C[i] // 2)
                C[i+2] += int(C[i] // 2)
            C[i] = 0
        elif C[i] >= 2 and C[i] % 2 == 1:
            liczba.append(1)
            if i+2 < len(C):
                C[i + 1] += int(C[i] // 2)
                C[i + 2] += int(C[i] // 2)
        print(C)
        print(liczba)
        print("-----------")
    return liczba


def solution(A, B):
    n = 0
    wynik = todec(A) + todec(B)
    binary = suma(A, B)
    print("A:", todec(A))
    print("B:", todec(B))
    print("Suma:", wynik)
    if wynik <= 0:
        while abs(wynik) > 2 ** n:
            n += 1
        n = n+2
    else:
        while abs(wynik) > 2 ** n:
            n += 1
        n = n+1
    print("N", n)
    print()
    print("negative binary:", binary[0:n])


if __name__ == "__main__":
    #A = [0,1,1,0,0,1,0,1,1,1,0,1,0,1,1]
    #B = [0,0,1,0,0,1,1,1,1,1,0,1]
    A = [1,0,0,1,1,1]
    B = [0,0,1]
    solution(A, B)