# bitwise operators (&,|,^)

print(1 & 0)

print(0 & 1)

print(0 & 0)

print(1 & 1)

print(1 | 0)

print(0 | 0)

print(0 | 1)

print(1 | 1)

print(0 ^ 0)

print(0 ^ 1)

print(1 ^ 1)

print(1 ^ 0)

print(3|4)
# 3 - 0011
# 4 - 0100
# --------
# 0111 - 7

print(4&3)
# 4 - 0100
# 3 - 0011
# --------
# 0000 - 0

print(2^3)
# 2 - 0010
# 3 - 0011
# --------
# 0001 - 1

# 0000
# msb - most significant bit
# lsb - least significant bit
# if msb is 0, number will be positive
# if msb is 1, number will be negative