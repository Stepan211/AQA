import pytest                       # Обязательно импортируем модуль

@pytest.fixture()                   # Используем фикстуру для предусловий тестов
def before_after():                 
    print("Before test")
    yield                           # Используется для возвращения результата теста
    print("\nAfter test")



def test_demo_1():
    assert 1 == 1


def test_demo_2(before_after):      # Пишем в скобках, что для этого теста, нужно выполнить предусловие и постусловие
    assert 2 == 2