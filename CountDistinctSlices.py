def solution(M, A):
    absolute_A = len(set([abs(i) for i in A]))
    print(absolute_A)
    return absolute_A


if __name__ == "__main__":
    M = 6
    A = [3,4,5,5,2]
    solution(A)