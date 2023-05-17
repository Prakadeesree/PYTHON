def is_pythagorean_triple(n1, n2, n3):
    if n1**2 + n2**2 == n3**2:
        return 1
    else:
        return 0

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

result = is_pythagorean_triple(n1, n2, n3)
print(result)
