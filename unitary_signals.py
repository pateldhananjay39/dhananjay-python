

import numpy as np
import matplotlib.pyplot as plt

def unit_step(n: int):
    
    time_index = np.arange(-n, n + 1)
    signal = np.where(time_index >= 0, 1, 0)
    plt.figure(figsize=(10, 6))
    plt.stem(time_index, signal)
    plt.title(f'Unit Step Signal u[n] for n = -{n} to {n}')
    plt.xlabel('n (Sample Index)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.ylim(-0.1, 1.2)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

    return signal

# ---

def unit_impulse(n: int):
  
    time_index = np.arange(-n, n + 1)
    signal = np.where(time_index == 0, 1, 0)
    plt.figure(figsize=(10, 6))
    plt.stem(time_index, signal)
    plt.title(f'Unit Impulse Signal δ[n] for n = -{n} to {n}')
    plt.xlabel('n (Sample Index)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.ylim(-0.1, 1.2) 
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

    return signal

# ---

def ramp_signal(n: int):
   
    time_index = np.arange(-n, n + 1)
    # Generate the signal: value equals the index for n >= 0
    signal = np.where(time_index >= 0, time_index, 0)

    # Plotting the discrete signal
    plt.figure(figsize=(10, 6))
    plt.stem(time_index, signal)
    plt.title(f'Ramp Signal r[n] for n = -{n} to {n}')
    plt.xlabel('n (Sample Index)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

    return signal

# ---

# Example usage block to demonstrate the functions
if __name__ == "__main__":
    # Define the range for the signals
    N_RANGE = 8

    print("--- 1. Generating Unit Step Signal ---")
    step_array = unit_step(N_RANGE)
    print(f"Returned NumPy array (length {len(step_array)}):\n", step_array)
    print("\n" + "="*50 + "\n")

    print("--- 2. Generating Unit Impulse Signal ---")
    impulse_array = unit_impulse(N_RANGE)
    print(f"Returned NumPy array (length {len(impulse_array)}):\n", impulse_array)
    print("\n" + "="*50 + "\n")

    print("--- 3. Generating Ramp Signal ---")
    ramp_array = ramp_signal(N_RANGE)
    print(f"Returned NumPy array (length {len(ramp_array)}):\n", ramp_array)
    print("\n" + "="*50 + "\n")