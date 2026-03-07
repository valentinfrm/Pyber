import auxiliary

def test_simple():
    integers = [5] * 256
    assert integers == auxiliary.byte_decode(auxiliary.byte_encode(integers, 12), 12)

def test_ascending():
    integers = list(range(256))
    print(integers)
    print(auxiliary.byte_encode(integers, 12))
    assert integers == auxiliary.byte_decode(auxiliary.byte_encode(integers, 12), 12)

