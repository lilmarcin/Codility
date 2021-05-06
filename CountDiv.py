"""
Write a function that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K. For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
A and B are integers within the range [0..2,000,000,000]; K is an integer within the range [1..2,000,000,000]; A ≤ B.
"""
import math
def solution(A, B, K):
    count = 0
    #for x in set(range(A, B+1)):
    #    print(x)
    count = math.floor(B/K) - math.ceil(A/K) + 1
    print("floor:", math.floor(B/K))
    print("ceil:", math.ceil(A/K))
    print("liczba:", count)
    return count


if __name__ == "__main__":
    solution(17, 26, 8)
