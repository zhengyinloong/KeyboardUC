# -*- coding:utf-8 -*-
# test6.py in KeyboardUC
# zhengyinloong
# 2023/10/17

import pyaudio
import matplotlib.pyplot as plt
import numpy as np


chunk = 512  # 缓冲区大小
format = pyaudio.paInt16  # 采样位数
channels = 1  # 声道数
rate = 44100  # 采样率
data = np.zeros(chunk, dtype=np.int16)

p = pyaudio.PyAudio()

stream = p.open(format=format,
                     channels=channels,
                     rate=rate,
                     input=True,
                     frames_per_buffer=chunk)

fig, ax = plt.subplots()
x = np.arange(0, 2 * chunk, 2)
ax.set_ylim(0, 100)
ax.set_xlim(0, chunk)
bar = ax.bar(1, 0, width=100)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
volume = 0

while True:
    data = stream.read(chunk)
    data_int = np.frombuffer(data, dtype=np.int16)
    volume = max(data_int) * 100 / 32768
    bar[0].set_height(volume)
    fig.canvas.draw()
    fig.canvas.flush_events()
    fig.show()

plt.close()
stream.stop_stream()
stream.close()
p.terminate()
