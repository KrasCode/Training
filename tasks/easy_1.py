def even_odd(n: int) -> str:
    """"
    Создать функцию которая принимает число и возвращает "Even" для чётных чисел и "Odd" для нечётных.
    """
    res = {
        0: 'Even',
        1: 'Odd'
    }
    return print(f'{n} -> {res[n % 2]}')


if __name__ == '__main__':
    even_odd(5)
