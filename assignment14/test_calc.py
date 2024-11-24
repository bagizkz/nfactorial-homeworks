# тестируем calc.py
from calc import calculate

def test_calculate():
    assert calculate(2, 3) == 5, "Ошибка: calculate(2, 3) должно быть 5"
    assert calculate(-1, 1) == 0, "Ошибка: calculate(-1, 1) должно быть 0"
    assert calculate(0, 0) == 0, "Ошибка: calculate(0, 0) должно быть 0"
    assert calculate(100, 200) == 300, "Ошибка: calculate(100, 200) должно быть 300"