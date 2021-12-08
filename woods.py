# Предлагаю решить вот такой вот арифметический ребус
#
# ДУБ + ДУБ + ... + ДУБ = РОЩА
#
# Разные буквы надо заменять на разные цифры
# Одинаковые буквы надо заменять на одинаковые цифры
#
# Вопрос:
# 1. Какое максимальное количество дубов может быть в роще?
# 2. Какое минимальное количество дубов может быть в роще?
# 3. Сколько всего решений у задачи?
# Взято из сообщества канала HashCoder (https://www.youtube.com/channel/UC-fVGFZ_v29h4yKShNBDMsg)
# https://www.youtube.com/post/UgkxtTcWFYMyDK1K1zcqXavZnZYwI6nCLA2e
from pprint import pprint


def brutforce(x: tuple = ()) -> list:
    result = []
    if len(x) == 7:
        oak = x[0] * 100 + x[1] * 10 + x[2]
        grove = x[3] * 1000 + x[4] * 100 + x[5] * 10 + x[6]
        if grove % oak == 0:
            return [(oak, grove // oak, grove)]
        else:
            return []
    for xi in range(0, 9):
        if not (xi in x):
        # if not (xi in x) and ((xi != 0) or ((len(x) != 0) and (len(x) != 3))):
            result.extend(brutforce(tuple(list(x)+[xi])))
    return result


combinate = brutforce()
pprint(combinate)
print(f'Count = {(len(combinate))}')
print(f'Minimum oaks = {min([i[1] for i in combinate])}')
print(f'Maximum oaks = {max([i[1] for i in combinate])}')