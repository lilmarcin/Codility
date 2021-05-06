def solution(A):
    if len(A) == 0:
        return -1
    sorted_A = sorted(A)
    print(sorted_A)
    polowa = len(A) // 2
    kandydat = sorted_A[polowa] #musi sie pojawic w ponad polowie listy czyli zawsze bedzie w polowie listy
    print('kandydat: ', kandydat)
    if A.count(kandydat) > polowa: #czy liczba z polowy pojawila sie wiecej razy niz polowa przedzialu
        print("Jest dominator o indeksie", A.index(kandydat), ' i jest to liczba: ', kandydat)
        return A.index(kandydat)
    return -1


if __name__ == "__main__":
    A = [1, 1, 1, 2, 3, 4, 1, 1,1, 1, -1, -2, -4]
    solution(A)