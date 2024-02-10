import math


def compute_roots(a, b, c):
    # Compute the discriminant
    discriminant = b ** 2 - 4 * a * c

    # Check if the discriminant is negative (no real roots)
    if discriminant < 0:
        return None, None

    # Compute the square root of the discriminant
    sqrt_discriminant = math.sqrt(discriminant)

    # Compute the roots
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)

    return x1, x2


# Given coefficients
a = 1.2
b = 2.3
c = -3.4

# Compute roots
root1, root2 = compute_roots(a, b, c)

# Print the roots
if root1 is not None and root2 is not None:
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    print("The quadratic equation has no real roots.")
