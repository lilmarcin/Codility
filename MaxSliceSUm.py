def solution(A):
    max_slice = 0
    ret_val = A[0]

    for value in A:
        max_slice = max(value, max_slice + value)
        ret_val = max(ret_val, max_slice)
    print(ret_val)
    return ret_val


if __name__ == "__main__":
    A = [3,2,-6,4,0]
    solution(A)