---
title: circle of filth
layout: post
---

```python

import wave
import math

from random import random

SECONDS = 2
BPM = 120

CHANNELS = 1
FRAMERATE = 48000
LOOPS = 2

d_note_frequency = {
    'C3': 130.81,
    'C#3': 138.59,
    'D3': 146.83,
    'D#3': 155.56,
    'E3': 164.81,
    'F3': 174.61,
    'F#3': 185.00,
    'G3': 196.00,
    'G#3': 207.65,
    'A3': 220.00,
    'A#3': 233.08,
    'B3': 246.94,
}

d_chord_notes = {
    'G#': ['C3', 'D#3', 'G#3'],
    'Cm': ['C3', 'D#3', 'G3'],
    'Fm': ['C3', 'F3', 'G#3'],
    'Gm': ['D3', 'G3', 'A#3'],
}


def add_chord(data, chord, offset):
    data += [0] * (SECONDS*FRAMERATE)
    amplitude = 255
    for note in d_chord_notes[chord]:
        for t in range(SECONDS*FRAMERATE):
            value = abs(math.cos(d_note_frequency[note]*t*2*math.pi/FRAMERATE)*amplitude)
            data[t+offset] += value
    return data, offset+SECONDS*FRAMERATE


data = []
offset = 0
data, offset = add_chord(data, 'Cm', offset)
data, offset = add_chord(data, 'G#', offset)
data, offset = add_chord(data, 'Fm', offset)
data, offset = add_chord(data, 'Gm', offset)

max_amp = max(data)
data = [(value / max_amp) * 255 for value in data]

data = [int(value) for value in data]

data = data*LOOPS
data = bytes(data)

with wave.open("output.wav", "wb") as f:
    f.setnchannels(CHANNELS)
    f.setsampwidth(1)
    f.setframerate(FRAMERATE)
    #f.setnframes(FRAMERATE*CHANNELS*SECONDS*CHORDS*LOOPS)
    f.setnframes(len(data))
    f.setcomptype('NONE', 'not compressed')
    f.writeframes(data)

```

```python

import wave
import math

SECONDS = 60
RESOLUTION = 100

CHANNELS = 1
FRAMERATE = 48000
SPACE = 5 * FRAMERATE

d_note_frequency = {
    'C3': 130.81,
    'C#3': 138.59,
    'D3': 146.83,
    'D#3': 155.56,
    'E3': 164.81,
    'F3': 174.61,
    'F#3': 185.00,
    'G3': 196.00,
    'G#3': 207.65,
    'A3': 220.00,
    'A#3': 233.08,
    'B3': 246.94,
}

d_chord_notes = {
    'F': ['C3', 'F3', 'G3'],
    'C': ['C3', 'E3', 'G3'],
    'G': ['D3', 'B3', 'G3'],
    'D': ['D3', 'F#3', 'A3'],
    'A': ['C#3', 'E3', 'A3'],
    'E': ['E3', 'G#3', 'B3'],
    'B': ['D#3', 'F#3', 'B3'],
    'F#': ['C#3', 'F#3', 'A#3'],
    'C#': ['C#3', 'F3', 'G#3'],
    'G#': ['C3', 'D#3', 'G#3'],
    'D#': ['D#3', 'G3', 'A#3'],
    'A#': ['D3', 'F3', 'A#3'],
    'Fm': ['C3', 'F3', 'G#3'],
    'Cm': ['C3', 'D#3', 'G3'],
    'Gm': ['D3', 'G3', 'A#3'],
    'Dm': ['D3', 'F3', 'A3'],
    'Am': ['C3', 'E3', 'A3'],
    'Em': ['E3', 'G3', 'B3'],
    'Bm': ['D3', 'F#3', 'B3'],
    'F#m': ['C#3', 'F#3', 'A3'],
    'C#m': ['C#3', 'E3', 'G#3'],
    'G#m': ['D#3', 'G#3', 'B3'],
    'D#m': ['D#3', 'F#3', 'A#3'],
    'A#m': ['C#3', 'F3', 'A#3'],
}

d_quinte = {
    'Fm': [],
    'Cm': [],
    'Gm': [],
    'Dm': [],
    'Am': [],
    'Em': [],
    'Bm': [],
    'F#m': [],
    'C#m': [],
    'G#m': [],
    'D#m': [],
    'A#m': []
}

def add_chord(chord):
    data = [0] * (SECONDS*FRAMERATE)
    amplitude = 80
    for note in d_chord_notes[chord]:
        for t in range(SECONDS*FRAMERATE):
            value = abs(math.cos(d_note_frequency[note]*t*2*math.pi/FRAMERATE)*amplitude)
            data[t] += value
    d_quinte[chord] = data

for chord in d_quinte:
    add_chord(chord)

chord_list = [chord for chord in d_quinte]
chord_list = chord_list + [chord_list[0]]

data = []
for t in range(SECONDS * FRAMERATE):
    whole, rest = int(t // SPACE), int(t % SPACE)
    actual_chord, next_chord = chord_list[whole], chord_list[whole+1]
    actual_percent = rest / SPACE
    next_percent = 1 - actual_percent
    value = d_quinte[actual_chord][t] * actual_percent + d_quinte[next_chord][t] * next_percent
    data.append(value)

max_amp = max(data)
#data = [(value / max_amp) * 255 for value in data]
data = [min(value, 255) for value in data]
data = [int(value) for value in data]
data = bytes(data)

with wave.open("output2.wav", "wb") as f:
    f.setnchannels(CHANNELS)
    f.setsampwidth(1)
    f.setframerate(FRAMERATE)
    f.setnframes(len(data))
    f.setcomptype('NONE', 'not compressed')
    f.writeframes(data)

```

2 -> m
3 -> m disto (remove comment)
4 -> M

bien split les code blocks

[output2](/wav/output2.wav)
