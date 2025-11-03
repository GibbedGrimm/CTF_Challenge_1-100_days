from math import gcd

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

plaintext = "CHEDDAR" # you can use other cheese name here
ciphertext = "ALUXXGH" # with respected cipher text

# Convert letters to numbers (A=0, B=1, ..., Z=25)
plaintext_val = [ord(c) - ord('A') for c in plaintext]
ciphertext_val = [ord(c) - ord('A') for c in ciphertext]

# Use first two letter pairs to set up equations
x1, y1 = plaintext_val[0], ciphertext_val[0]  # C=2, A=0
x2, y2 = plaintext_val[1], ciphertext_val[1]  # H=7, D=3

# Solve for a: (y1 - y2) = a * (x1 - x2) mod 26
diff_x = (x1 - x2) % 26
diff_y = (y1 - y2) % 26

# Find modular inverse of diff_x
inv_diff_x = mod_inverse(diff_x, 26)
affine_a = None
if inv_diff_x is not None:
    affine_a = (diff_y * inv_diff_x) % 26

# Solve for b using first letter pair: y1 = (a * x1 + b) mod 26
affine_b = None
if affine_a is not None:
    affine_b = (y1 - (affine_a * x1)) % 26

# Verify the parameters
if affine_a is not None and affine_b is not None:
    # Check if the affine cipher maps all letters correctly
    valid = all((affine_a * p + affine_b) % 26 == c for p, c in zip(plaintext_val, ciphertext_val))
    if valid:
        print(f"Found affine cipher parameters: a = {affine_a}, b = {affine_b}")
    else:
        print("Parameters do not map plaintext to ciphertext correctly")
else:
    print("Could not find a suitable (a, b) pair")