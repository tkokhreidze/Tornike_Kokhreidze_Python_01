import numpy as np
from colorama import Fore, init

# Initialize colorama
init()

# Create 2 matrices (3x5) A and B with values from 0 to 14
A = np.arange(15).reshape(3, 5)
B = np.arange(15).reshape(3, 5)

print(Fore.BLUE, A)

print()

# Transpose matrix A to get a new matrix with dimensions 5x3
A_transposed = A.T
print(Fore.RED, A_transposed)

print()

# Rotate matrix A 90 degrees counterclockwise
A_rotated_90_ccw = np.rot90(A, 1)
print(Fore.GREEN, A_rotated_90_ccw)

print()

# Rotate matrix A 180 degrees
A_rotated_180 = np.rot90(A, 2)
print(Fore.GREEN, A_rotated_180)

print()

# Rotate matrix A 90 degrees clockwise
A_rotated_90 = np.rot90(A, -1)
print(Fore.GREEN, A_rotated_90)

print()


# Mirror matrix A vertically
A_mirrored_vertical = np.flipud(A)
print(Fore.GREEN, A_mirrored_vertical)

print()

# Mirror matrix A horizontally
A_mirrored_horizontal = np.fliplr(A)
print(Fore.GREEN, A_mirrored_horizontal)

print()

A = np.arange(1, 21).reshape(4, 5)
print(Fore.WHITE, A)

print()

B = np.full((4, 5), 2)
print(Fore.WHITE, B)

print()

# Horizontally stack A and B to create a new matrix AB with dimensions 4x10
AB = np.hstack((A, B))
print(Fore.WHITE, AB)

print()

# Vertically stack A and B to create a new matrix with dimensions 8x5
AB_vertical = np.vstack((A, B))
print(Fore.YELLOW, AB_vertical)

print()

# Vertically stack [A, B] with [B, A] to create a new matrix with dimensions 8x10
AB_combined = np.vstack((AB, np.hstack((B, A))))
print(Fore.YELLOW, AB_combined)

print()

# Element-wise multiplication of A and B
B = np.full((5, 4), 2)
A_B_multiplication = np.dot(A, B)
print(Fore.YELLOW, A_B_multiplication)
