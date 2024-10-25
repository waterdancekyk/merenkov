def average_and_check(array):

    avg = round(sum(array) / len(array))

    contains_one = '1' in str(avg)
    contains_five = '5' in str(avg)

    if contains_one:
        print("Я хороший программист")
    if contains_five:
        print("Преподаватель - красавчик")
    
    return avg


def main():
    case1 = list(map(int, input("Введите числа для первого массива через пробел: ").split()))
    case2 = list(map(int, input("Введите числа для второго массива через пробел: ").split()))

    avg1 = average_and_check(case1)
    avg2 = average_and_check(case2)

    print(f"Среднее первого массива: {avg1}")
    print(f"Среднее второго массива: {avg2}")


if __name__ == "__main__":
    main()
