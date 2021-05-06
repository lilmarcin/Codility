def solution(A):
    absolute_A = len(set([abs(i) for i in A]))
    print(absolute_A)
    return absolute_A




if __name__ == "__main__":
    A = [-5,-3,-1,0,3,6]
    solution(A)