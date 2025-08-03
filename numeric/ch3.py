import math
def maximum(f, xl, xu, iter):
    iterations = []
    for i in range(iter):
        d = 0.618 * (xu - xl)
        x1 = xl + d
        x2 = xu - d
        fx1 = f(x1)
        fx2 = f(x2)
        iterations.append({
            "i": i,
            "xl": xl,
            "f(xl)": f(xl),
            "xu": xu,
            "f(xu)": f(xu),
            "x1": x1,
            "f(x1)": fx1,
            "x2": x2,
            "f(x2)": fx2,
            "d": d
        })
        if fx1 < fx2:
            xu = x1
        elif fx1 > fx2:
            xl = x2
    if fx1 < fx2:
        max = x2
    else:
        max = x1
    return max, iterations
    
def minimum(f, xl, xu, iter):
    iterations = []
    for i in range(iter):
        d = 0.618 * (xu - xl)
        x1 = xl + d
        x2 = xu - d
        fx1 = f(x1)
        fx2 = f(x2)
        iterations.append({
            "i": i,
            "xl": xl,
            "f(xl)": f(xl),
            "xu": xu,
            "f(xu)": f(xu),
            "x1": x1,
            "f(x1)": fx1,
            "x2": x2,
            "f(x2)": fx2,
            "d": d
        })
        if fx1 < fx2:
            xl = x2
        elif fx1 > fx2:
            xu = x1
    if fx1 < fx2:
        min = x1
    else:
        min = x2
    return min, iterations