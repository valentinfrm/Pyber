# Pyber – ML-KEM (Kyber)
This project is a Python implementation of the ML-KEM (Kyber) key encapsulation mechanism.
The goal of this project is to understand the underlying concepts.
## Features
- Key generation, encapsulation, decapsulation
- Polynomial arithmetic over $\mathbb{Z}_{q}[x]/(x^n + 1)$
- Number Theoretic Transform (NTT) and inverse NTT
- NTT-based polynomial multiplication
- Sampling (CBD, rejection sampling)

## Structure
- `kem.py` - ML-KEM interface
- `pke.py` - underlying public key encryption
- `sampling.py` - noise sampling, matrix expansion
- `polynomial.py` - polynomial representation and operations
- `ntt.py` - NTT, inverse NTT, NTT-based multiplication

## Usage
## Implementation Notes
## Performance
## What I Learned