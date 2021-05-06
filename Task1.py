import math

def solution(A, B):
    maks_krawedz = math.floor((A + B) // 4)
    sticks_A = 0
    sticks_B = 0
    suma = 0
    wynik = 0
    result = []
    if maks_krawedz < 1:
        return 0
    for i in range(1, maks_krawedz+1):
        print(i)
        sticks_A = int((A / i))
        sticks_B = int((B / i))
        suma = sticks_A + sticks_B
        print("Suma", sticks_A, sticks_B)
        if suma >= 4:
            result.append(i)
            wynik = i
    print("maksymalna dlugosc: ", result)
    return max(result)



if __name__ == "__main__":
    A = 13
    B = 11
    solution(A, B)