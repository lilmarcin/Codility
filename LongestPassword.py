def solution(S):
    dlugosc = -1
    letters = 0
    digits = 0
    others = 0
    splitted = S.split(' ')
    print(splitted)
    for litera in splitted:
        for i in range(len(litera)):
            if litera[i].isalpha():
                letters += 1
            elif litera[i].isdigit():
                digits += 1
            else:
                others += 1
        print("Slowo ma {} dlugosci i zawiera: {} liter, {} cyfr i {} innych znakow".format(letters + digits + others, letters, digits, others))
        if others == 0 and letters % 2 == 0 and digits % 2 == 1:
            if letters + digits > dlugosc:
                dlugosc = letters + digits
                print("Nowa dlugosc: ", dlugosc, " Slowo: ", )
        letters = 0
        digits = 0
        others = 0
    print("Najdluzsze haslo ma {} znakow".format(dlugosc))
    return dlugosc


if __name__ == "__main__":
    S = "test 5 a0A pass007 ?xy1"
    solution(S)