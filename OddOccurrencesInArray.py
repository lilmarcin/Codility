"""
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.
"""


def solution(A):
    print("Lista:", A)
    if len(A) == 1:
        return A[0]
    A = sorted(A)
    print("Lista po sortowaniu:", A)
    for i in range(0, len(A), 2):
        if i + 1 == len(A):
            print("Liczba bez pary:", A[i])
            return A[i]
        if A[i] != A[i + 1]:
            print("Liczba bez pary:", A[i])
            return A[i]


if __name__ == "__main__":
    A = [9, 3, 9, 3, 9, 7, 9]
    solution(A)
