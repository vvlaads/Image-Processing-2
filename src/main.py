import random
from math import sqrt
from methods import *


def function(x):
    """Функция f(x) = x^2"""
    return x ** 2


def p1(x, start, end):
    """Нормированная плотность вероятности p(x) ~ x"""
    c = 2 / (end ** 2 - start ** 2)
    return c * x


def inverse_p1(tau, start, end):
    """Обратная функция распределения (inverse CDF) для p(x) ~ x"""
    return sqrt(tau * (end ** 2 - start ** 2) + start ** 2)


def p2(x, start, end):
    """Нормированная плотность вероятности p(x) ~ x^2"""
    c = 3 / (end ** 3 - start ** 3)
    return c * x ** 2


def inverse_p2(tau, start, end):
    """Обратная функция распределения (inverse CDF) для p(x) ~ x^2"""
    return (tau * (end ** 3 - start ** 3) + start ** 3) ** (1 / 3)


def p3(x, start, end):
    """Нормированная плотность вероятности"""
    c = 4 / (end ** 4 - start ** 4)
    return c * x ** 3


def inverse_p3(tau, start, end):
    """Обратная функция распределения (inverse CDF) для p(x) ~ x^3"""
    return (tau * (end ** 4 - start ** 4) + start ** 4) ** 0.25


a = 2
b = 5
integral = 39

rng = random.Random(42)
print(f"Значение интеграла: {integral}")
print(f"Простой метод Монте-Карло: {monte_carlo_function(rng, a, b, function)}")
print(f"Метод Монте-Карло со стратификацией: {monte_carlo_function_with_stratification(rng, a, b, function)}")
print(f"Метод Монте-Карло с выборкой по значимости (x): "
      f"{monte_carlo_function_with_sampling_by_significance(rng, a, b, function, p1, inverse_p1)}")
print(f"Метод Монте-Карло с выборкой по значимости (x^2): "
      f"{monte_carlo_function_with_sampling_by_significance(rng, a, b, function, p2, inverse_p2)}")
print(f"Метод Монте-Карло с выборкой по значимости (x^3): "
      f"{monte_carlo_function_with_sampling_by_significance(rng, a, b, function, p3, inverse_p3)}")
