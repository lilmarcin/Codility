def NWD(a, b):
    if a % b == 0:
        print("NWD ", a, " i ", b, " wynosi ", b)
        return b
    else:
        print("NWD ", a, " i ", b, " wynosi ", NWD(b, a % b))
        return NWD(b, a % b)


def solution(N, M):
    count = int(N / NWD(N, M)) #po ilu razach dostaniemy wielokrotnosc liczby N
    print(count)
    return count


if __name__ == "__main__":
    N = 10
    M = 5
    solution(N, M)