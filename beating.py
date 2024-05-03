import numpy as np
def beating(duration=5, sample_rate=44100, frequency1=440, frequency2=442, volume=0.4):
    # Generate time array
    t = np.linspace(0, duration, int(duration * sample_rate), False)

    # Generate sine waves for left and right channels
    left_channel = np.sin(2 * np.pi * frequency1 * t)
    right_channel = np.sin(2 * np.pi * frequency2 * t)

    # Combine left and right channels into a stereo signal
    stereo_signal = np.column_stack((left_channel, right_channel))
    stereo_signal *= volume
    return stereo_signal
    