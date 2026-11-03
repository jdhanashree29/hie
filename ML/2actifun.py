
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 500)

functions = [
    ("Sigmoid", lambda x: 1/(1+np.exp(-x))),
    ("Tanh", np.tanh),
    ("ReLU", lambda x: np.maximum(0, x)),
    ("Leaky ReLU", lambda x: np.where(x>0, x, 0.01*x)),
    ("PReLU", lambda x: np.where(x>0, x, 0.25*x)),
    ("RReLU", lambda x: np.where(x>0, x, 0.23*x)),
    ("ELU", lambda x: np.where(x>0, x, np.exp(x)-1)),
    ("SELU", lambda x: 1.0507*np.where(x>0, x, 1.67326*(np.exp(x)-1))),
    ("Softplus", lambda x: np.logaddexp(0, x)),
    ("Softsign", lambda x: x/(1+np.abs(x))),
    ("Swish", lambda x: x/(1+np.exp(-x))),
    ("Hard Swish", lambda x: x*np.clip((x+3)/6, 0, 1)),
    ("Mish", lambda x: x*np.tanh(np.logaddexp(0, x))),
    ("GELU", lambda x: 0.5*x*(1+np.vectorize(
        __import__('math').erf)(x/np.sqrt(2)))),
    ("Hard Sigmoid", lambda x: np.clip((x+3)/6, 0, 1)),
    ("Hard Tanh", lambda x: np.clip(x, -1, 1)),
    ("TanhShrink", lambda x: x-np.tanh(x)),
    ("SoftShrink", lambda x: np.where(x>0.5, x-0.5,
                              np.where(x < -0.5, x+0.5, 0))),
    ("HardShrink", lambda x: np.where(np.abs(x)>0.5, x, 0)),
    ("Linear", lambda x: x)
]

plt.figure(figsize=(15, 12))

for i, (name, func) in enumerate(functions, 1):
    plt.subplot(4, 5, i)
    plt.plot(x, func(x))
    plt.title(name)
    plt.grid(True)
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)

plt.tight_layout()
plt.show()
