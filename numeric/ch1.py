import math

def check_validation(f, xl, xu):
    if f(xl) * f(xu) > 0:
        return False
    return True

def bisection_method(f, xl, xu, stop_type='eps', value=0.01):
    iterations = []  # Collect iteration data
    if xl > xu:
        xl, xu = xu, xl
    if not check_validation(f, xl, xu):
        return None, iterations
    iter = 0
    xr_old = 0
    if stop_type == 'iter':
        max_iter = value
        while True:
            xr = (xl + xu) / 2
            error = abs((xr - xr_old) / xr) * 100 if xr != 0 else 0
            iterations.append({
                "i": iter,
                "xl": xl,
                "f(xl)": f(xl),
                "xu": xu,
                "f(xu)": f(xu),
                "xr": xr,
                "f(xr)": f(xr),
                "error": error
            })
            if f(xl) * f(xr) < 0:
                xu = xr
            else:
                xl = xr
            if iter >= max_iter:
                break
            xr_old = xr
            iter += 1
    else:
        eps = value
        while True:
            xr = (xl + xu) / 2
            error = abs((xr - xr_old) / xr) * 100 if xr != 0 else 0
            iterations.append({
                "i": iter,
                "xl": xl,
                "f(xl)": f(xl),
                "xu": xu,
                "f(xu)": f(xu),
                "xr": xr,
                "f(xr)": f(xr),
                "error": error
            })
            if f(xl) * f(xr) < 0:
                xu = xr
            else:
                xl = xr
            if error < eps:
                break
            xr_old = xr
            iter += 1
    return xr, iterations

def false_position(f, xl, xu, stop_type='eps', value=0.01):
    iterations = [] 
    if xl > xu:
        xl, xu = xu, xl
    if not check_validation(f, xl, xu):
        return None, iterations
    iter = 0
    xr_old = 0
    if stop_type == 'iter':
        max_iter = value
        while True:
            xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
            error = abs((xr - xr_old) / xr) * 100 if xr != 0 else 0
            iterations.append({
                "i": iter,
                "xl": xl,
                "f(xl)": f(xl),
                "xu": xu,
                "f(xu)": f(xu),
                "xr": xr,
                "f(xr)": f(xr),
                "error": error
            })
            if f(xl) * f(xr) < 0:
                xu = xr
            else:
                xl = xr
            if iter >= max_iter:
                break
            xr_old = xr
            iter += 1
    else:
        eps = value
        while True:
            xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
            error = abs((xr - xr_old) / xr) * 100 if xr != 0 else 0
            iterations.append({
                "i": iter,
                "xl": xl,
                "f(xl)": f(xl),
                "xu": xu,
                "f(xu)": f(xu),
                "xr": xr,
                "f(xr)": f(xr),
                "error": error
            })
            if f(xl) * f(xr) < 0:
                xu = xr
            else:
                xl = xr
            if error < eps:
                break
            xr_old = xr
            iter += 1
    return xr, iterations

def fixed_point(g, x0, stop_type='eps', value=0.01):
    iterations = [] 
    iter = 0
    if stop_type == 'iter':
        max_iter = value
        while True:
            x1 = g(x0)
            error = abs((x1 - x0) / x1) * 100
            iterations.append({
                "i": iter,
                "xi": x0,
                "g(xi)": g(x0),
                "xi+1": x1,
                "error": error
            })
            if iter >= max_iter:
                break
            x0 = x1
            iter += 1
    else:
        eps = value
        while True:
            x1 = g(x0)
            error = abs((x1 - x0) / x1) * 100
            iterations.append({
                "i": iter,
                "xi": x0,
                "g(xi)": g(x0),
                "xi+1": x1,
                "error": error
            })
            if error < eps:
                break
            x0 = x1
            iter += 1
    return x1, iterations

def newton_method(f, f_dash, x0, stop_type='eps', value=0.01):
    iterations = []
    iter = 0
    if stop_type == 'iter':
        max_iter = value
        while True:
            f_x = f(x0) 
            f_dash_x = f_dash(x0)
            x1 = x0 - f_x / f_dash_x
            error = abs((x1 - x0) / x1) * 100
            iterations.append({
                "i": iter,
                "xi": x0,
                "f(xi)": f_x,
                "f’(xi)": f_dash_x,
                "xi+1": x1,
                "error": error
            })
            if iter >= max_iter:
                break
            x0 = x1
            iter += 1
    else:
        eps = value
        while True:
            f_x = f(x0)
            f_dash_x = f_dash(x0)
            x1 = x0 - f_x / f_dash_x
            error = abs((x1 - x0) / x1) * 100
            iterations.append({
                "i": iter,
                "xi": x0,
                "f(xi)": f_x,
                "f’(xi)": f_dash_x,
                "xi+1": x1,
                "error": error
            })
            if error < eps:
                break
            x0 = x1
            iter += 1
    return x1, iterations

def secant(f, x0, x1, stop_type='eps', value=0.01):
    iterations = []
    iter = 0
    if stop_type == 'iter':
        max_iter = value
        while True:
            f0 = f(x0)
            f1 = f(x1)
            x2 = x1 - f1 * (x0 - x1) / (f0 - f1)
            error = abs((x2 - x1) / x2) * 100
            iterations.append({
                "i": iter,
                "xi-1": x0,
                "f(xi-1)": f0,
                "xi": x1,
                "f(xi)": f1,
                "xi+1": x2,
                "error": error
            })
            if iter >= max_iter:
                break
            x0, x1 = x1, x2 #x0=x1, x1=x2
            iter += 1
    else:
        eps = value
        while True:
            f0 = f(x0)
            f1 = f(x1)
            x2 = x1 - f1 * (x0 - x1) / (f0 - f1)
            error = abs((x2 - x1) / x2) * 100
            iterations.append({
                "i": iter,
                "xi-1": x0,
                "f(xi-1)": f0,
                "xi": x1,
                "f(xi)": f1,
                "xi+1": x2,
                "error": error
            })
            if error < eps:
                break
            x0, x1 = x1, x2 #x0=x1, x1=x2
            iter += 1
    return x2, iterations