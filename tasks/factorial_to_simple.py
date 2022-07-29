"""
Дано число n. Необходимо разложить факториал этого число
на простые множители и представить результат в строковом виде.
n = 12
Ответ: 2^10 * 3^5 * 5^2 * 7 * 11
"""


def isPrime(num: int) -> bool:
    if num % 2 == 0:
        return num == 2
    prime = 3
    while prime * prime <= num and num % prime != 0:
        prime += 1
    return prime * prime > num


def listForNotPrime(num, lst=None):
    if lst is None:
        lst = list()
    for el in range(2, num + 1):
        if num % el == 0:
            lst.append(el)
            if num == el:
                return lst
            else:
                return listForNotPrime(int(num / el), lst)


def addDictPrime(num, dPrime):
    lstFact = (x for x in range(2, num + 1))
    for elem in lstFact:
        if isPrime(elem):
            dPrime[elem] = 1
        else:
            for el in listForNotPrime(elem):
                dPrime[el] += 1
    return dPrime


if __name__ == '__main__':
    dictPrime = dict()
    addDictPrime(22, dictPrime)
    list_view = [str(k) if v == 1 else str(k) + '^' + str(v) for k, v in dictPrime.items()]
    view_numb = ' * '.join(list_view)
    print(view_numb)
