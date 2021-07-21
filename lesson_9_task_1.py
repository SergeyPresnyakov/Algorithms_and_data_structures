"""1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана
строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib
задача считается не решённой."""


def search_substring(string):
    assert len(string) > 0, "Строка должна быть не пустой"
    hashs_strings = set('')
    for i in range(len(string) + 1):
        for j in range(len(string) + 1):
            if len(string) != len(string[i:j]):
                hashs_strings.add(hash(string[i:j]))

    hashs_strings.discard(0)
    print(f"Количесвто различных подстрок в строке '{string}' равно {len(hashs_strings)}")


string = input("Введите строку: ")
search_substring(string)




