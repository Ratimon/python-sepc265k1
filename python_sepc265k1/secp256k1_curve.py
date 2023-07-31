def is_on_secp256k1_curve(n):
    # secp256k1 parameters
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    b = 7

    # Convert coordinates to integers
    x, y = n

    # Calculate y^2 (mod p)
    y_squared = pow(y, 2, p)

    # Calculate x^3 + 7 (mod p)
    x_cubed_plus_7 = (pow(x, 3, p) + b) % p

    # Check if y^2 ≡ x^3 + 7 (mod p)
    return y_squared == x_cubed_plus_7

# Test cases
valid_point1 = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
valid_point2 = (0xF4A3F22A48F469FDDBC4FF057D66A0DC2D7C022C404F5F22A8EB0330F00C7975, 0x23AD5EBE0F7A6CF43AB8C5B2E6D27FB7F7FB7E4CE2CC9EB48D6EE22C2308C3E3)
invalid_point1 = (0x0, 0x0)
invalid_point2 = (0x2A7B3EEB7B01C3CE1455C88A0043AE814D66B50BB7239C3DEADA84EB3CB5986A, 0x0)

print("Valid Point 1:", is_on_secp256k1_curve(valid_point1))  # True
print("Valid Point 2:", is_on_secp256k1_curve(valid_point2))  # True
print("Invalid Point 1:", is_on_secp256k1_curve(invalid_point1))  # False
print("Invalid Point 2:", is_on_secp256k1_curve(invalid_point2))  # False

