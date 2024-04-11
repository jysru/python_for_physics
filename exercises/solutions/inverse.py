import math

def naive_inverse(x: float) -> float:
    return 1 / x

def aware_inverse(x: float) -> float:
    try:
        y = naive_inverse(x)
    except ZeroDivisionError:
        y = math.inf
    return y

def result(x: float) -> None:
    print(aware_inverse(x))