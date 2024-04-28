import matplotlib.pyplot as plt
import numpy as np

def deutchs():
    # Define two frequencies (replace with desired illusion notes)
    f1 = 440  # Hz (A4)
    f2 = 493.88  # Hz (B4)

    # Sample rate
    sample_rate = 22050

    # Duration of each illusion segment (seconds)
    segment_duration = 2

    # Generate time axis
    t = np.arange(0, segment_duration * sample_rate) / sample_rate

    # Create two segments with different rising or falling sequences
    segment_1 = np.sin(2 * np.pi * f1 * t)  # Segment 1 with constant F1
    segment_2 = np.sin(2 * np.pi * f1 * t[:int(segment_duration * sample_rate / 2)]) + \
                np.sin(2 * np.pi * f2 * t[int(segment_duration * sample_rate / 2):])  # Segment 2 with rising frequency

    # Plot both segments
    plt.plot(t, segment_1, label="Segment 1 (Constant)")
    plt.plot(t, segment_2, label="Segment 2 (Rising)")

    # Label and display the plot
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.title("Visual Representation of Deutsch's Scale Illusion (Constant vs. Rising Sequence)")
    plt.show()

    print("This script generates a visual representation of the Deutsch's scale illusion. \nListen to recordings of the illusion to experience the auditory effect.")
