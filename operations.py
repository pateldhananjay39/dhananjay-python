import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal, k):
    
    shifted_signal = np.roll(signal, k)
   
    if k > 0:
        shifted_signal[:k] = 0
    elif k < 0:
        shifted_signal[k:] = 0

    plt.figure()
    plt.plot(signal, label='Original Signal')
    plt.plot(shifted_signal, label=f'Shifted Signal by {k}')
    plt.title(f"Time Shift by {k} units")
    plt.xlabel("Sample index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

    return shifted_signal

def time_scale(signal, k):
   
    n = len(signal)
    indices = np.arange(0, n, 1/k)
    indices = indices[indices < n]

    scaled_signal = np.interp(indices, np.arange(n), signal)

    plt.figure()
    plt.plot(signal, label='Original Signal')
    plt.plot(np.arange(len(scaled_signal)), scaled_signal, label=f'Scaled Signal by {k}')
    plt.title(f"Time Scale by factor {k}")
    plt.xlabel("Sample index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

    return scaled_signal

def signal_addition(signal1, signal2):
    
    min_len = min(len(signal1), len(signal2))
    added_signal = signal1[:min_len] + signal2[:min_len]

    plt.figure()
    plt.plot(signal1[:min_len], label='Signal 1')
    plt.plot(signal2[:min_len], label='Signal 2')
    plt.plot(added_signal, label='Added Signal')
    plt.title("Signal Addition")
    plt.xlabel("Sample index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

    return added_signal

def signal_multiplication(signal1, signal2):
    
    min_len = min(len(signal1), len(signal2))
    multiplied_signal = signal1[:min_len] * signal2[:min_len]

    plt.figure()
    plt.plot(signal1[:min_len], label='Signal 1')
    plt.plot(signal2[:min_len], label='Signal 2')
    plt.plot(multiplied_signal, label='Multiplied Signal')
    plt.title("Signal Multiplication")
    plt.xlabel("Sample index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

    return multiplied_signal


if __name__ == "__main__":

    t = np.linspace(0, 2 * np.pi, 100)
    sig1 = np.sin(t)
    sig2 = np.cos(t)

    time_shift(sig1, 10)
    time_scale(sig1, 2)
    signal_addition(sig1, sig2)
    signal_multiplication(sig1, sig2)
