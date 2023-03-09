---
title: marie theory
---

#### introduction

![mm](/img/mm.png)
{:.ioda}

#### simplification

![mm 2](/img/mm_2.png)
{:.ioda}

---

![mm 3](/img/mm_3.png)
{:.ioda}

#### esthétisation

![mm 4](/img/mm_4.png)
{:.ioda}

v et vii majeurs en min

#### programmation

output

```

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

#### composition

...
