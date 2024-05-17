# https://www.codewars.com/kata/559a28007caad2ac4e000083
def fibonacci_gen():
    fib1 = fib2 = 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


def perimeter(n):
    f = fibonacci_gen()
    sum_n = 0
    for i in range(1, n + 2):
        sum_n += next(f)
    return 4 * sum_n


print(perimeter(5) == 80)
print(perimeter(7) == 216)
print(perimeter(20) == 114624)
print(perimeter(30) == 14098308)
print(perimeter(100) == 6002082144827584333104)
print(perimeter(
    500) == 2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504)
