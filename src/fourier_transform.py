import numpy as np
import matplotlib.pyplot as plt

def apply_fourier_transform(signal, sample_rate):
    """Apply Fourier transform and plot the frequency spectrum."""
    freqs = np.fft.fftfreq(len(signal), 1/sample_rate)
    spectrum = np.fft.fft(signal)
    plt.figure()
    plt.plot(freqs, np.abs(spectrum))
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.show()

# Use the signal from sound_generation.py
# Assume 'sound' is imported or accessible
apply_fourier_transform(sound, 44100)
