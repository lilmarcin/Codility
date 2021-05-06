"""


A string S consisting of N characters is called properly nested if:

        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..1,000,000];
        string S consists only of the characters "(" and/or ")".


"""
def solution(S):
    tymczasowa = []
    opening = ['(']
    closing = [')']
    for i in S:
        if i in opening:
            tymczasowa.append(i)
        elif i in closing:
            if len(tymczasowa) < 1:
                print("brak nawiasow otwierajacych:", )
                return 0
            ostatni = tymczasowa.pop()
            print("Ostatni nawias: ", ostatni)
            if opening.index(ostatni) != closing.index(i):
                print("zle nawiasy:", opening.index(ostatni), closing.index(i))
                return 0
            print("nawiasy:", opening.index(ostatni), closing.index(i))
    if len(tymczasowa) == 0:
        return 1
    return 0




if __name__ == "__main__":
    A = "(()(())())"
    solution(A)