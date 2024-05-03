import os
import random
import time
from shepards import shepards, tritone
import sounddevice as sd
# from beating import beating
from music21 import midi
from beating import beating
import simpleaudio as sa
from music21 import stream, instrument
from music21.note import Note
import numpy as np

def playIllusion():
    cwd = os.getcwd()
    # Play the Shepard's illusion
    choose = [True, True, False]
    choice = True
    while choice:
        # Play the Shepard's illusion ascending
        num1 = int(random.uniform(1, 4))
        num2 = 5 - num1
        shepard_scale = shepards(num1, 0.5, rise = choice)
        player = midi.realtime.StreamPlayer(shepard_scale)
        player.play()
        #noise insertion
        num_noise_samples = int(.2 * 44100)
        noise = np.random.normal(0, .6, num_noise_samples)
        sd.play(noise, blocking=True)
        sd.wait()
        #Remainder of scale
        shepard_scale = shepards(num2, 0.5, rise = choice)
        player = midi.realtime.StreamPlayer(shepard_scale)
        player.play()
        # Play the tritone paradox
        player = midi.realtime.StreamPlayer(tritone(2, loop=5))
        player.play()
        # Play beating illusion
        sd.play(beating(), blocking=True)
        # Randomly choose to play again
        choice = random.choice(choose)
        print('Playing again...')
    shepard_scale = shepards(7, 0.5, rise = False)
    player = midi.realtime.StreamPlayer(shepard_scale)
    player.play()
    path = os.path.join(cwd, "Deutsch_scale_illusion.wav")
    wave_obj = sa.WaveObject.from_wave_file(path)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    # play a C5 pitch with a quick bit of noise in the middle, 
    # matching pitch of Deustch scale illusion ending
    # Should simulate discontinuity illusion.
    signal = generateBrokenPitch()
    sd.play(signal, blocking=True)
    print('Done')    
    
def generateBrokenPitch(frequency=523.25, duration=8, sampling_rate=44100, noise_duration=0.1, noise_amplitude=0.1):
    time = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * time)
    # Generate Gaussian noise
    num_noise_samples = int(noise_duration * sampling_rate)
    noise = np.random.normal(0, noise_amplitude, num_noise_samples)
    # Choose a random starting point within the signal
    start_index = np.random.randint(0, len(signal) - num_noise_samples)
    # Add the noise to the signal at the random starting point
    signal_with_noise = signal.copy()
    signal_with_noise[start_index:start_index + num_noise_samples] += noise
    return signal_with_noise * .4

playIllusion()