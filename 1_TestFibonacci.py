def is_fibonacci(n):
    #aqui gera um Fibonacci ate o numero n
    def generate_fibonacci(limit):
        fib_sequence = [0, 1]
        while fib_sequence[-1] < limit:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

    fibonacci_sequence = generate_fibonacci(n)

    #verifica se o numero esta na sequencia
    if n in fibonacci_sequence:
        return f"{n} pertence à sequência de Fibonacci."
    else:
        return f"{n} não pertence à sequência de Fibonacci."

number = int(input("Informe um número: "))
result = is_fibonacci(number)
print(result)
