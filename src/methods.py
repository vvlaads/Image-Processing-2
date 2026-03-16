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


def monte_carlo_function_with_multiple_sampling_by_significance(rng, a, b, f, p1, inverse_p1, p2, inverse_p2,
                                                                weights_type=WeightType.BALANCE, n_samples=1000):
    """Интегрирование методом Монте-Карло с многократной выборкой по значимости"""
    total = 0
    prob = 0.5

    for _ in range(n_samples):
        if rng.random() < prob:
            tau = rng.random()
            xi = inverse_p1(tau, a, b)

            if weights_type == WeightType.BALANCE:
                weight = balance_heuristic(p1, p2, xi, 1, a, b)
            else:
                weight = power_heuristic(p1, p2, xi, 1, a, b)

            total += weight * f(xi) / (prob * p1(xi, a, b))
        else:
            tau = rng.random()
            xi = inverse_p2(tau, a, b)

            if weights_type == WeightType.BALANCE:
                weight = balance_heuristic(p1, p2, xi, 2, a, b)
            else:
                weight = power_heuristic(p1, p2, xi, 2, a, b)

            total += weight * f(xi) / (prob * p2(xi, a, b))

    return total / n_samples


def monte_carlo_function_with_russian_roulette(rng, a, b, f):
    """Интегрирование методом Монте-Карло с использованием русской рулетки"""
    return monte_carlo_function(rng, a, b, f)
