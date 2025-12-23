from math import log10


# 1
def greetings(username:str='User') -> str:
    """A function that greetings User.

    :param username: Custom username by user. `Username` is **User** by default.
    :return: str
    """
    return f'\nGreetings, {username}'

# 2
def souvenirs_and_trinkets(souvenirs_number: int = 0,
                           trinkets_number: int = 0,
                           souvenirs_mass: int = 75,
                           trinkets_mass: int = 112) -> str:
    """A function that summarize weight of purchase."""
    return f'\n\tРассчитанный вес покупки: {(souvenirs_number * souvenirs_mass
                            + trinkets_number * trinkets_mass)}'

# 3
def complicated_percents(first_deposit: int = 0,
                         percent: int = 4,
                         years: int = 3) -> str:
    """A function that count on the amount of money in the user's account
    for several years"""
    answer = f'\nПри условии {percent}% годовых.'

    for year in range(1,years+1):
        amount = first_deposit * percent / 100
        answer += (f'\n{year} год '
                   f'у вкладчика накопится '
                   f'{round(first_deposit + amount, 2)} '
                   f'на счету.')
        first_deposit += amount
    return answer

# 4
def arithmetic(a: int = 0, b: int = 0) -> str:
    """A function that match difference arithmetic tasks"""
    return (f'\n\tСумма a+b: {a+b}'
            f'\n\tРазница a-b: {a-b}'
            f'\n\tПроизведение a*b: {a*b}'
            f'\n\tЧастное от деления: {a//b}'
            f'\n\tОстаток от деления: {a%b}'
            f'\n\tДесятичный логарифм числа а: {log10(a)}'
            f'\n\tРезультат возведения числа a в степень b: {a**b}')

# 5
def cashbox(cash_sum: int = 0) -> str:
    """A function that return the number of required coin."""
    answer = ''
    main_sum = cash_sum

    coins_rubles = {
        500: '5 рублей',
        200: '2 рублей',
        100: '1 рублей',
        50: '50 копеек',
        5: '5 копеек',
        1: '1 копейка',
    }

    # Создаём лист монет разного номинала
    coins_variation = [500, 200, 100, 50, 5, 1]
    # Создаём лист с нулевым номиналом по количеству монет
    coins_count = [0] * len(coins_variation)

    # Заполняем список монет, сколько найдено момент максимально номинала
    for i, coin in enumerate(coins_variation):
        # Сопоставляем основную сумму с максимальным номиналом и в случае,
        # если сумма больше, просто
        if main_sum >= coin:
            coins_count[i] =  main_sum // coin
            main_sum -= coins_count[i] * coin

    # Перебор количества монет и создание выражения "номинал-количество" монет
    for i, count in enumerate(coins_count):
        if count != 0:
            answer += (f'\n\tНоминалом: {coins_rubles[coins_variation[i]]} - '
                       f'Количество: {count}')

    return (f'\n\tДля пользовательской суммы: {cash_sum} копеек\n'
            f'\tнеобходимо выдать монет номиналом:\n\n'
            f'{answer}')


def full_bread(old_bread_count: int = 0, bread_cost: int = 49, discount: int = 60) -> str:
    """A function that calculate the cost of bread"""
    old_bread_cost = bread_cost - bread_cost * 60 / 100
    return (f'\nСтоимость свежей буханки: {bread_cost}'
            f'\nСтоимость вчерашней буханки со скидкой: '
            f'{old_bread_cost}'
            f'\nОбщая стоимость вчерашнего хлеба: '
            f'{old_bread_count * old_bread_cost}')


def main():
    """A main function that gives options to choice for the user."""
    # Выбор пользователем задания
    result: str
    while True:
        try:
            selection = input('\n---\nВыберите задачу с 1-6 или '
                              'exit чтобы выйти\n--> ')
            if selection != 'exit':
                selection = int(selection)
            match selection:
                case 1:
                    print(greetings(input('\nВведите своё имя --> ')))
                case 2:
                    souvenirs_count = int(input('\nВведите количество '
                                                'желаемых сувениров --> '))
                    trinkets_count = int(input('\nВведите количество '
                                               'желаемых безделушек --> '))
                    print(f'{souvenirs_and_trinkets(souvenirs_count, 
                                                    trinkets_count)}г')
                case 3:
                    print(complicated_percents(int(input('\nВведите сумму '
                                                            'первоначального '
                                                            'депозита --> '))))
                case 4:
                    print(arithmetic(
                        int(input('\nВведите первое число --> ')),
                        int(input('\nВведите второе число --> '))
                    ))
                case 5:
                    print(cashbox(
                        int(input('\nВведите сумму сдачи в копейках --> ')))
                    )
                case 6:
                    print(full_bread(int(input('\nУкажите желаемое '
                                               'количество хлеба --> '))))
                case 'exit':
                    break
                case '_':
                    continue

        except ValueError:
            print('\n---\nВведите корректное запрашиваемое значение!')


if __name__ == '__main__':
    main()
