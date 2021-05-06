def solution(A):
    min_price = 1000000
    max_profit = 0
    for i in A:
        min_price = min([min_price, i])
        max_profit = max([max_profit, i - min_price])
        print(i - min_price)
    print("MAX PROFIT:", max_profit, "KUPIC W DNIU: ", A.index(min_price), "SPRZEDAC W DNIU: ", A.index(i))
    return max_profit


if __name__ == "__main__":
    A = [23171,21011,21123,21366,21013,21367]
    solution(A)