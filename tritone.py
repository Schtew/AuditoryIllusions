import numpy as np
from midiutil import MIDIFile

def tritone():
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

    # Create MIDIFile object
    mf = MIDIFile(1, adjust_origin=False)

    # Add tempo track
    track = 0
    time = 0
    mf.addTrackName(track, time, "Stereo Signal")
    mf.addTempo(track, time, 120)  # Tempo in BPM

    # Add notes for left channel
    for i, note in enumerate(left_channel):
        velocity = int(abs(note) * 127)  # Velocity depends on the amplitude of the signal
        mf.addNote(track, 0, i, int(note * 127), int(duration * sample_rate), velocity)

    # Add notes for right channel
    for i, note in enumerate(right_channel):
        velocity = int(abs(note) * 127)  # Velocity depends on the amplitude of the signal
        mf.addNote(track, 1, i, int(note * 127), int(duration * sample_rate), velocity)

    # Save the MIDI file
    with open("stereo_signal.mid", "wb") as outf:
        mf.writeFile(outf)
