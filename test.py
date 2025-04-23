from Ass_1 import Secant_method, ge

def print_matrix(mat):
    for row in mat:
        print("  ".join(f"{num:8.3f}" for num in row))
    print()

# Example system:
# x + y + z = 6
# 2y + 5z = -4
# 2x + 5y - z = 27
matrix = [
    [2, 0, 0, 1],
    [1, 1, 0, 2],
    [0, 3, 1, 3]
]

# Run Gaussian Elimination
result = ge(matrix)

# Output the result
print("Reduced matrix:")
print_matrix(result)

if __name__ == "__main__":
    # Example function for Secant method
    function = "x**2 - 4"
    x0 = 1.0
    x1 = 2.0

    # Run Secant method
    result = Secant_method(function, x0, x1)
    print(f"Root found: {result}")