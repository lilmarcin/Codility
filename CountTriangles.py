def solution(A):
    # write your code in Python 3.6
    A.sort()
    count = 0
    if len(A) < 3:
        return 0
    for i in range(0, len(A)-2):
        for j in range(i+1, len(A)-1):
            for k in range(j+1, len(A)):
                print("i: ", i, " j: ", j, " k: ", k)
                if A[i] + A[j] > A[k]:
                    count += 1
                    print("Count:", count)
    return count


if __name__ == "__main__":
    A = [10,2,5,1,8,12]
    solution(A)