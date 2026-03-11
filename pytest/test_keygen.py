from kyber_py.ml_kem import ML_KEM_768

"""not working untill NTT ig
def test_equal():
    d = bytes(32)
    z = bytes(32)
    x1, y1 = keygen.pke_keygen(d)
    x2, y2 = ML_KEM_768.key_derive(d + z)
    assert x1 == x2  # ek
    assert y1 == y2  # dk
"""