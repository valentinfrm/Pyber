def bytes_to_bits(byte_array):
    result = []
    for b in byte_array:
        for i in range(8):
            result.append(b >> (7 - i) & 1)
    return result

def bits_to_bytes(bit_array):
    result = []
    for i in range(len(bit_array) // 8): # cuts off remaining bits if len(bit_array) % 8 != 0
        x = 0
        for j in range(8):
            x += bit_array[i * 8 + j] * 2**j
        result.append(x)
    return result