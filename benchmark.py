import timeit

from kyber_py.ml_kem import ML_KEM_512, ML_KEM_768, ML_KEM_1024
import matplotlib.pyplot as plt
import numpy as np

from pyber import params
from pyber.kem import keygen, encaps, decaps

RUN_AMOUNT = 20

color_1 = "#DCD6F7"
color_2 = "#424874"
color_3 = "#2ecc71"
color_4 = "#e74c3c"
color_5 = "#00b4d8"
color_6 = "#ef233c"
color_7 = "#212121"
color_8 = "#7192ED"
color_9 = "#C7DD4C"
color_10 = "#14591D"
color_11 = "#0a3082"
color_12 = "#fa3a24"
color_13 = "#ff9db9"
color_14 = "#2b4273"
color_15 = "#3B83FF"
color_16 = "#B0C9FF"
color_17 = "#CCDCFF"

k_map = {
    "ML-KEM-512":  {"k": 2, "eta1": 3, "du": 10, "dv": 4},
    "ML-KEM-768":  {"k": 3, "eta1": 2, "du": 10, "dv": 4},
    "ML-KEM-1024": {"k": 4, "eta1": 2, "du": 11, "dv": 5},
}

def to_ms(time):
    return round(time / RUN_AMOUNT * 1000, 2) # round to 2 decimal points

def set_params(version):
    for key, value in k_map[version].items():
        setattr(params, key, value) # sets params.key = value

result = {
    "pyber": {} ,
    "kyber_py": {}
}

# ===== 512 =====
set_params("ML-KEM-512")
ek, dk = keygen()
K, c = encaps(ek)

# globals make module-level names available to timeit
result["pyber"]["512-keygen"] = to_ms(min(timeit.repeat('keygen()', number=RUN_AMOUNT, globals=globals())))
result["pyber"]["512-encaps"] = to_ms(min(timeit.repeat('encaps(ek)', number=RUN_AMOUNT, globals=globals())))
result["pyber"]["512-decaps"] = to_ms(min(timeit.repeat('decaps(dk, c)', number=RUN_AMOUNT, globals=globals())))

ek, dk = ML_KEM_512.keygen()
K, c = ML_KEM_512.encaps(ek)

result["kyber_py"]["512-keygen"] = to_ms(min(timeit.repeat('ML_KEM_512.keygen()', number=RUN_AMOUNT, globals=globals())))
result["kyber_py"]["512-encaps"] = to_ms(min(timeit.repeat('ML_KEM_512.encaps(ek)', number=RUN_AMOUNT, globals=globals())))
result["kyber_py"]["512-decaps"] = to_ms(min(timeit.repeat('ML_KEM_512.decaps(dk, c)', number=RUN_AMOUNT, globals=globals())))

# ===== 768 =====
set_params("ML-KEM-768")
ek, dk = keygen()
K, c = encaps(ek)

result["pyber"]["768-keygen"] = to_ms(min(timeit.repeat('keygen()', number=RUN_AMOUNT, globals=globals())))
result["pyber"]["768-encaps"] = to_ms(min(timeit.repeat('encaps(ek)', number=RUN_AMOUNT, globals=globals())))
result["pyber"]["768-decaps"] = to_ms(min(timeit.repeat('decaps(dk, c)', number=RUN_AMOUNT, globals=globals())))

ek, dk = ML_KEM_768.keygen()
K, c = ML_KEM_768.encaps(ek)

result["kyber_py"]["768-keygen"] = to_ms(min(timeit.repeat('ML_KEM_768.keygen()', number=RUN_AMOUNT, globals=globals())))
result["kyber_py"]["768-encaps"] = to_ms(min(timeit.repeat('ML_KEM_768.encaps(ek)', number=RUN_AMOUNT, globals=globals())))
result["kyber_py"]["768-decaps"] = to_ms(min(timeit.repeat('ML_KEM_768.decaps(dk, c)', number=RUN_AMOUNT, globals=globals())))

# ===== 1024 =====
set_params("ML-KEM-1024")
ek, dk = keygen()
K, c = encaps(ek)

result["pyber"]["1024-keygen"] = to_ms(min(timeit.repeat('keygen()', number=RUN_AMOUNT, globals=globals())))
result["pyber"]["1024-encaps"] = to_ms(min(timeit.repeat('encaps(ek)', number=RUN_AMOUNT, globals=globals())))
result["pyber"]["1024-decaps"] = to_ms(min(timeit.repeat('decaps(dk, c)', number=RUN_AMOUNT, globals=globals())))

ek, dk = ML_KEM_1024.keygen()
K, c = ML_KEM_1024.encaps(ek)

result["kyber_py"]["1024-keygen"] = to_ms(min(timeit.repeat('ML_KEM_1024.keygen()', number=RUN_AMOUNT, globals=globals())))
result["kyber_py"]["1024-encaps"] = to_ms(min(timeit.repeat('ML_KEM_1024.encaps(ek)', number=RUN_AMOUNT, globals=globals())))
result["kyber_py"]["1024-decaps"] = to_ms(min(timeit.repeat('ML_KEM_1024.decaps(dk, c)', number=RUN_AMOUNT, globals=globals())))

def print_result():
    for imp, values in result.items():
        print(f"=== {imp} ====")
        for key, value in values.items():
            print(f"{key}: {value}")

# ===== plotting =====
def get_data(op):
    sizes = ["512", "768", "1024"]

    pyber_data = [result["pyber"][f"{s}-{op}"] for s in sizes]
    kyber_py_data = [result["kyber_py"][f"{s}-{op}"] for s in sizes]

    return pyber_data, kyber_py_data

def plot(op, ax):
    versions = ["512 Bit", "768 Bit", "1024 Bit"]
    x = np.arange(len(versions)) # creates [0, 1, 2 ...]
    pyber_data, kyber_py_data = get_data(op)
    w = 0.2 # bar width

    bar_1 = ax.bar(x-w/2, width=w, height=pyber_data, label="Pyber", color=color_16)
    bar_2 = ax.bar(x+w/2, width=w, height=kyber_py_data, label="Kyber-py", color=color_15)

    ax.bar_label(bar_1)
    ax.bar_label(bar_2)
    ax.set_xticks(x)
    ax.set_xticklabels(versions)
    ax.set_title(f"{op}()")
    ax.yaxis.set_major_locator(plt.MultipleLocator(1))  # large steps
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25)) # small steps
    ax.yaxis.grid(True, alpha=0.2)
    ax.set_axisbelow(True) # moves yaxis grid behind bars

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
plt.rcParams['font.family'] = 'monospace'

plot("keygen", ax1)
plot("encaps", ax2)
plot("decaps", ax3)

fig.suptitle(
    f"pyber vs. kyber-py | Apple M1 | macOS | min of {RUN_AMOUNT} runs",
    # y=0.95,
    fontsize=20,
    fontweight='bold'
    )
ax1.legend(loc='upper left')
ax1.set_ylabel("ms")

plt.tight_layout()
plt.show()