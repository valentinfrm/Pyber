import auxiliary

def test_simple():
    integers = auxiliary.byte_encode(12, [5] * 256)
    assert integers == auxiliary.byte_decode(12, auxiliary.byte_encode(12, integers))

def test_ascending():
    integers = list(range(256))
    print(integers)
    print(auxiliary.byte_encode(12, integers))
    assert integers == auxiliary.byte_decode(12, auxiliary.byte_encode(12, integers))

