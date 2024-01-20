# Bytes type
# Use of bytes operators
# The byte operator is a byte unit operator
# The byte operator is the byte type

b = bytes([0, 16, 32, 48, 64])
print(b)
print(type(b))
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])


# ASCII and bytes type

b = bytes([0x00, 0x10, 0x20, 0x30, 0x40])
print(b)
print(type(b))
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[0:3])
print(b[0:5])


# Convert string to bytes

s = 'Hello'
b = s.encode()
print(b)
print(type(b))

b= b'Hello'
print(b)
print(type(b))

