"""
Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].


"""
def solution(A):
    A.sort()
    print(A)
    A_filtered = list(filter(lambda x: x > 0, A))
    print(A_filtered)
    length = len(A_filtered)
    if length == 0 or A_filtered[0] != 1:
        print("Same ujemne lub zbior pusty lub jedna cyfra rozna od 1, najmniejszy integer to 1")
        return 1
    for i in range(len(A_filtered)-1):
        print(i)
        if A_filtered[i+1] - A_filtered[i] > 1:
            print("Najmniejszy integer: ", A_filtered[i]+1)
            return A_filtered[i]+1
    print("Wszystko jest po kolei, najmniejszy integer: ", A_filtered[-1]+1)
    return A_filtered[-1]+1
if __name__ == "__main__":
    N = 5
    A = [-1,-3]
    solution(A)