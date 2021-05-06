"""


A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

        The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
        The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
        The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:

    def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P, Q is an integer within the range [0..N − 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.


"""
def solution(S, P, Q):
    N = len(S)
    M = len(P)
    wynik = [0] * M
    pos_A = [0] * (N)
    pos_C = [0] * (N)
    pos_G = [0] * (N)
    pos_T = [0] * (N)
    for i in range(0, N):
        if (S[i] == 'A'):
            pos_A[i] = 1
        if (S[i] == 'C'):
            pos_C[i] = 1
        if (S[i] == 'G'):
            pos_G[i] = 1
        if (S[i] == 'T'):
            pos_T[i] = 1
    print("String: ", S)
    print("A:", pos_A)
    print("C:", pos_C)
    print("G:", pos_G)
    print("T:", pos_T)
    for i in range(0, M):
        lancuch_i = set()
        if P[i] <= Q[i]:
            for j in range(P[i], Q[i]+1):
                print("literka numer ", j)
                if (S[j] == 'A'):
                    lancuch_i.add(1)
                elif (S[j] == 'C'):
                    lancuch_i.add(2)
                elif (S[j] == 'G'):
                    lancuch_i.add(3)
                elif (S[j] == 'T'):
                    lancuch_i.add(4)
            print("Lancuch utworzony z M[", i, "]: ", lancuch_i)
            if 1 in lancuch_i:
                wynik[i] = 1
            elif 2 in lancuch_i:
                wynik[i] = 2
            elif 3 in lancuch_i:
                wynik[i] = 3
            elif 4 in lancuch_i:
                wynik[i] = 4
    print(wynik)
    return wynik
if __name__ == "__main__":
    S = "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
    P = [0, 0, 1]
    Q = [0, 5, 20]
    solution(S, P, Q)