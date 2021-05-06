def solution(H):
    mur = []
    bloki = 0
    for wysokosc in H:
        while mur and mur[-1] > wysokosc:
            mur.pop()
        if not mur or mur[-1] <wysokosc:
            mur.append(wysokosc)
            bloki += 1
            print('Mur ma juz ' + str(bloki))
            print('')
        print()
    return bloki




if __name__ == "__main__":
    A = [8,8,5,7,9,8,7,4,8]
    solution(A)