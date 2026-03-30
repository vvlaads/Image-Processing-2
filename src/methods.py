from weights_type import *


def monte_carlo_function(rng, a, b, f):
    """Простое интегрирование методом Монте-Карло"""
    xi = rng.uniform(a, b)
    return (b - a) * f(xi)


def monte_carlo_function_with_stratification(rng, a, b, f, step=0.5):
    """Интегрирование методом Монте-Карло со стратификацией"""
    borders = [a]

    while borders[-1] + step < b:
        borders.append(borders[-1] + step)

    borders.append(b)

    s = 0
    for i in range(len(borders) - 1):
        start = borders[i]
        end = borders[i + 1]
        s += monte_carlo_function(rng, start, end, f)

    return s


def monte_carlo_function_with_sampling_by_significance(rng, a, b, f, p, inverse_p):
    """Интегрирование методом Монте-Карло с выборкой по значимости"""
    tau = rng.random()
    xi = inverse_p(tau, a, b)
    return f(xi) / p(xi, a, b)


def monte_carlo_function_with_multiple_sampling_by_significance(
        rng, a, b, f, p1, inverse_p1, p2, inverse_p2,
        weights_type=WeightType.BALANCE):
    """Интегрирование методом Монте-Карло с многократной выборкой по значимости"""
    tau = rng.random()
    xi1 = inverse_p1(tau, a, b)
    xi2 = inverse_p2(tau, a, b)

    if weights_type == WeightType.BALANCE:
        weight1 = balance_heuristic(p1, p2, xi1, 1, a, b)
        weight2 = balance_heuristic(p1, p2, xi2, 2, a, b)
    else:
        weight1 = power_heuristic(p1, p2, xi1, 1, a, b)
        weight2 = power_heuristic(p1, p2, xi2, 2, a, b)

    return weight1 * f(xi1) / (p1(xi1, a, b)) + weight2 * f(xi2) / (p2(xi2, a, b))


def monte_carlo_function_with_russian_roulette(rng, a, b, f, r):
    """Интегрирование методом Монте-Карло с использованием русской рулетки"""
    xi = rng.uniform(a, b)
    r1 = (a + (b - a) * r)
    if xi > r1:
        return 0
    return (r1 - a) * f(xi / r) / r
