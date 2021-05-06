def solution(A): #wstawianie
    print("Przed sortowaniem: ", A)
    for i in range(len(A)):
        for j in range(i):
            if A[i] < A[j]:
                A[j], A[i] = A[i], A[j]
                print("Sortowanie: ", A)
    print("Posortowana tablica: ", A)


def solution2(A): #babelkowe
    print("Przed sortowaniem: ", A)
    for i in range(len(A)):
        for j in range(len(A) - 1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                print("Sortowanie: ", A)
    print("Posortowana tablica: ", A)

if __name__ == "__main__":
    A = [14,5,7,1,21,12]
    solution2(A)