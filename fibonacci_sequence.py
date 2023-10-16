def fibonacci_sequence(n):

    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        a = 0
        b = 1

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            sequence.append(c)
        return sequence

n = int(input("Enter number: "))
print(fibonacci_sequence(n))

