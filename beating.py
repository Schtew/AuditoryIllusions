import numpy as np
import sounddevice as sd

def beating():
    # Audio parameters
    duration = 5  # Duration in seconds
    sample_rate = 44100  # Sample rate
    frequency1 = 440  # Frequency for the left channel
    frequency2 = 442  # Frequency for the right channel (slightly higher)

    # Generate time array
    t = np.linspace(0, duration, int(duration * sample_rate), False)

    # Generate sine waves for left and right channels
    left_channel = np.sin(2 * np.pi * frequency1 * t)
    right_channel = np.sin(2 * np.pi * frequency2 * t)

    # Combine left and right channels into a stereo signal
    stereo_signal = np.column_stack((left_channel, right_channel))

    # Play the stereo signal
    sd.play(stereo_signal, blocking=True)