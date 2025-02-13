def fibonacci(n):
    first, second = 0, 1
    for _ in range(n):
        print(first, end=" ")
        next_term = first + second
        first, second = second, next_term
    print()


num_terms = int(input("Enter the number of terms: "))


print("Fibonacci Series:", end=" ")
fibonacci(num_terms)