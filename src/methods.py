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


def monte_carlo_function_with_multiple_sampling_by_significance(rng, a, b, f, p):
    """Интегрирование методом Монте-Карло с многократной выборкой по значимости"""
    return monte_carlo_function(rng, a, b, f)


def monte_carlo_function_with_russian_roulette(rng, a, b, f):
    """Интегрирование методом Монте-Карло с использованием русской рулетки"""
    return monte_carlo_function(rng, a, b, f)
