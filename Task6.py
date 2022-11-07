import concurrent.futures as pool

# Задание 6. Используя модуль concurrent.futures, распараллельте на процессы процедуру вычисления выборочной дисперсии трех чисел. 
# Написанное приложение должно быть консольным. 
# Аргументы командной строки – три числа.


def get_mean(n1: float, n2: float, n3: float) -> float:
    return (n1+n2+n3)/3


def get_square_devitation(n: float, mean: float) -> float:
    return (n-mean)**2


def get_variance(n1: float, n2: float, n3: float) -> float:
    return (n1+n2+n3)/2


if __name__ == "__main__":
    n1 = float(input('Input first number: '))
    n2 = float(input('Input second number: '))
    n3 = float(input('Input third number: '))
    mean = get_mean(n1, n2, n3)
    with pool.ThreadPoolExecutor(max_workers=4) as executer:
        sd1 = executer.submit(get_mean, n1, n2, n3)
        sd2 = executer.submit(get_square_devitation, n1, mean)
        sd3 = executer.submit(get_square_devitation, n2, mean)
        sd4 = executer.submit(get_square_devitation, n3, mean)
        result = executer.submit(get_variance, float(sd2.result()), float(sd3.result()), float(sd4.result()) )
        print(result.result())


