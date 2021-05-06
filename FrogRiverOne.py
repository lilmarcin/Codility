def solution(X, A):
    ilosc_lisci = set([i for i in range(1, X + 1)])
    print("ilosc lisci do przebycia: ", ilosc_lisci)
    droga = set()
    for sekunda, pokryty_lisc in enumerate(A):
        if pokryty_lisc <= X:
            droga.add(pokryty_lisc)
            print("Droga:", droga, "po ", sekunda, " sekundzie/sekundach")
        if ilosc_lisci == droga:
        #if[item for item in droga if item in ilosc_lisci]:
            print("Czas po ktorym ostatni lisc spadnie: ", sekunda)
            return sekunda
    print("Nie spadla wystarczajaca ilosc lisci: ")
    return -1



if __name__ == "__main__":
    X = 3
    A = [1,3,1,4,2,3,5,4,6,1,7,8,9,1,10]
    solution(X, A)