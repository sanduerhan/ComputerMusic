import pyaudio
import numpy as np

p = pyaudio.PyAudio()

SRATE = 44100  # sampling rate
TYPE = np.float32
A = 880
B = 987.767
C = 523.251
D = 587.33
E = 659.255
F = 698.456
G = 783.991
a = A*2
b = B*2
c = C*2
d = D*2
e = E*2
f = F*2
g = G*2
pairs = [(G, 0.5),(G, 0.5),(A, 1), (G, 1), (c, 1), (B, 2), (G, 0.5),(G, 0.5),
(A, 1), (G, 1),(d, 1), (c, 2),(G, 0.5),(G, 0.5),(g, 1), (e, 1), (c, 1), (B, 1), (A, 1), (f, 0.5), (f, 0.5),
(e, 1), (c, 1), (d, 1), (c, 2)]
def osc(frec,dur,vol):   
    return vol*np.sin(2*np.pi*np.arange(int(SRATE*dur))*frec/SRATE)

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=SRATE,
                output=True)

for a, b in pairs:
    samples = osc(a,b,0.5)
    stream.write(samples.astype(TYPE).tobytes())

stream.stop_stream()
stream.close()

p.terminate()

