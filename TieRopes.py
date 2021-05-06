def solution(K, A):
    dlugosc = 0
    count = 0
    for i in A:
        dlugosc += i #dodajemy nastepne dlugosci az do uzyskania wiecej niz K
        print("Dlugosc liny: ",dlugosc)
        if dlugosc >= K:
            count += 1
            dlugosc = 0 #szukamy kolejnych sekwencji lin dlatego reset
            print("Osiagnieto zamierzona dlugosc, zwiekszamy count i szukamy dalej")
    print(count)
    return count


if __name__ == "__main__":
    K = 4
    A = [2,1,1,1,1,4]
    solution(K,A)