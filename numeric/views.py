from django.shortcuts import render
from django.http import HttpResponse
from .ch1 import (bisection_method, false_position, fixed_point, newton_method, secant) 
from .ch2 import (gauss_elimination, gauss_jordan_elimination, gauss_elimination_partial_pivoting, gauss_jordan_partial_pivoting, lu_decomposition, lu_decomposition_partial_pivoting, cramer)
from .ch3 import (maximum, minimum)
def home(request):
    return render(request, 'numeric/index.html')

def ch1(request):
    selected_method = request.GET.get('method', 'bisection')
    return render(request, 'numeric/ch1.html', {'selected_method': selected_method})

def ch2(request):
    selected_method = request.GET.get('method', 'gauss-elimination')
    return render(request, 'numeric/ch2.html', {'selected_method': selected_method})

def ch3(request):
    selected_method = request.GET.get('method', 'golden-section')
    return render(request, 'numeric/ch3.html', {'selected_method': selected_method})

    
def calculate_ch1(request):
    if request.method == 'POST':
        function = request.POST.get('function')
        xl = float(request.POST.get('x0'))
        xu = float(request.POST.get('x1'))
        stop_type = request.POST.get('stop_type')
        method = request.POST.get('method')  # Get the selected method

        # Define the function to be used in the methods
        f = lambda x: eval(function)
        
        if stop_type == 'eps':
            value = float(request.POST.get('epsilon_value', 0.01))  # Default to 0.01 if not provided
        elif stop_type == 'iter':
            value = int(request.POST.get('iteration_value', 10))  # Default to 10 if not provided
        
        if method == 'bisection':
            result, iterations = bisection_method(f, xl, xu, stop_type, value)
        elif method == 'false_position':
            result, iterations = false_position(f, xl, xu, stop_type, value)
        elif method == 'fixed_point':
            g_function = request.POST.get('g_function')
            if not g_function:
                return HttpResponse("Error: Missing g_function for Fixed-Point method.")
            g = lambda x: eval(g_function)
            result, iterations = fixed_point(g, xl, stop_type, value)
        elif method == 'newton_method':
            f_dash_function = request.POST.get('f_dash_function')
            if not f_dash_function:
                return HttpResponse("Error: Missing f_dash_function for Newton-Raphson method.")
            f_dash = lambda x: eval(f_dash_function)
            result, iterations = newton_method(f, f_dash, xl, stop_type, value)
        elif method == 'secant':
            result, iterations = secant(f, xl, xu, stop_type, value)
        
        if iterations:
            table_headers = list(iterations[0].keys())  # Dynamic headers from the first row
        else:
            table_headers = []

        return render(request, 'numeric/ch1.html', {
            'root': result,
            'iterations': iterations,
            'headers': table_headers
        })
    return HttpResponse("Invalid request method.")

def calculate_ch2(request):
    if request.method == 'POST':
        matrix = request.POST.get('matrix')
        matrix = [list(map(float, row.split())) for row in matrix.splitlines() if row.strip()]
        method = request.POST.get('method')  # Get the selected method
        use_pivoting = request.POST.get('partial-pivoting') == '1'
        
        result = None
        logs = None
        # Adjust method based on pivoting
        if use_pivoting:
            if method == 'gauss-elimination':
                method = 'gauss-elimination-partial-pivoting'
            elif method == 'gauss-jordan':
                method = 'gauss-jordan-partial-pivoting'
            elif method == 'lu-decomposition':
                method = 'lu-decomposition-partial-pivoting'
        
        if method == 'gauss-elimination':
            result, logs = gauss_elimination(matrix)
        elif method == 'gauss-jordan':
            result, logs = gauss_jordan_elimination(matrix)
        elif method == 'lu-decomposition':
            L, U, result, logs = lu_decomposition(matrix)
        elif method == 'cramer':
            result, logs = cramer(matrix)
        elif method == 'gauss-elimination-partial-pivoting':
            result, logs = gauss_elimination_partial_pivoting(matrix)
        elif method == 'gauss-jordan-partial-pivoting':
            result, logs = gauss_jordan_partial_pivoting(matrix)
        elif method == 'lu-decomposition-partial-pivoting':
            L, U, P, result, logs = lu_decomposition_partial_pivoting(matrix)

        return render(request, 'numeric/ch2.html', {
            'result': result,
            'matrix': matrix,
            'logs': logs,
            'headers': ['Step', 'Matrix'] if logs else [],
            'method': method
        })
    return HttpResponse("Invalid request method.")

def calculate_ch3(request):
    if request.method == 'POST':
        function = request.POST.get('function')
        xl = float(request.POST.get('xl'))
        xu = float(request.POST.get('xu'))
        iter = int(request.POST.get('iterations'))
        method = request.POST.get('method')  # Get the selected method

        # Define the function to be used in the methods
        f = lambda x: eval(function)

        if method == 'max':
            result, iterations = maximum(f, xl, xu, iter)
        elif method == 'min':
            result, iterations = minimum(f, xl, xu, iter)

        if iterations:
            table_headers = list(iterations[0].keys())  # Dynamic headers from the first row
        else:
            table_headers = []

        return render(request, 'numeric/ch3.html', {
            'result': result,
            'iterations': iterations,
            'headers': table_headers
        })
    return HttpResponse("Invalid request method.")