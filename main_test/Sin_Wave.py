import numpy as np
import matplotlib.pyplot as plt

def sine_wave(frequency=440, amplitude=1, duration=1, sample_rate=44100):
    """
    Generates a sine wave with specified frequency, amplitude, duration, and sample rate.

    Args:
        frequency (float): Frequency of the sine wave in Hz.
        amplitude (float): Amplitude of the sine wave.
        duration (float): Duration of the sine wave in seconds.
        sample_rate (int): Sampling rate in Hz.

    Returns:
        numpy.ndarray: Array representing the sine wave.
    """
    time_axis = np.linspace(0, duration, int(duration * sample_rate))
    waveform = amplitude * np.sin(2 * np.pi * frequency * time_axis)
    return waveform

def plot_sine_wave(waveform, sample_rate, frequency, title="Sine Wave"):
    """
    Plots a sine wave using matplotlib.

    Args:
        waveform (numpy.ndarray): The sine wave data.
        sample_rate (int): Sampling rate of the waveform.
        frequency (float): Frequency of the sine wave.
        title (str, optional): Plot title.
    """
    time_axis = np.linspace(0, len(waveform) / sample_rate, len(waveform))
    plt.plot(time_axis, waveform)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(f"{title}, {frequency} Hz")
    plt.show()

# Example usage
wave = sine_wave(frequency=440, amplitude=0.5)
plot_sine_wave(wave, sample_rate=44100, frequency=440)

#test hold