"""
Пишем декораторы
"""


def uppercase(func):
    """Функция декоратор
    Делает вывод прописными буквами
    """

    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


def strong(func):
    """Функция декоратор
    Оборачивает текст в тег <strong>"""

    def wrapper():
        return "<strong>" + func() + "</strong>"

    return wrapper


def emphasis(func):
    """Функция декторатор
    Оборачивает текст в тег <em>"""

    def wrapper():
        return "<em>" + func() + "</em>"

    return wrapper


@strong
@emphasis
def greet():
    """Тестовая функция
    Выводит приветствие
    """
    return "Привет!"


print(greet())
