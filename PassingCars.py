

def solution(A):
    going_east = 0
    passed_cars = 0
    for i in A:
        if i == 0:
            going_east += 1
            print("auto jedzie w prawo: ", going_east)
        else:
            passed_cars += going_east
            print("auto jedzie w lewo: ", passed_cars)
            if passed_cars > 10**9:
                return -1
    print(passed_cars)
    return passed_cars

if __name__ == "__main__":
    A = [0,1,0,1,1]
    solution(A)