import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

def generate_sine_wave(frequency, duration, sample_rate=44100):
    """Generate a sine wave for a given frequency and duration."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * frequency * t)

def save_sound(sound, filename, sample_rate=44100):
    """Save sound to a WAV file."""
    scaled = np.int16(sound/np.max(np.abs(sound)) * 32767)
    write(filename, sample_rate, scaled)

# Example usage
frequency = 440  # A4
sound = generate_sine_wave(frequency, 2)
save_sound(sound, 'A4_note.wav')
