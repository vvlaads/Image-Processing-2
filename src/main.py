import random

from methods import *


def function(x):
    """Функция f(x) = x^2"""
    return x ** 2


a = 2
b = 5
integral = 39

rng = random.Random(42)
print(f"Значение интеграла: {integral}")
print(f"Простой метод Монте-Карло: {monte_carlo_function(rng, a, b, function)}")
print(f"Метод Монте-Карло со стратификацией: {monte_carlo_function_with_stratification(rng, a, b, function)}")
