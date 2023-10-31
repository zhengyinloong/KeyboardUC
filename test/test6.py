# -*- coding:utf-8 -*-
# test6.py in KeyboardUC
# zhengyinloong
# 2023/10/17

import pyaudio
import matplotlib.pyplot as plt
import numpy as np

chunk = 1024  # 缓冲区大小
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

# rate = 44100
# start = 0
# # 开始采样位置
# df = framerate / (rate - 1)
# # 分辨率
# freq = [df * n for n in range(0, rate)]
# # N个元素
# wave_data2 = wave_data[0][start:start + rate]
# c = np.fft.fft(wave_data2) * 2 / rate
# # 常规显示采样频率一半的频谱
# plt.subplot(212)
# plt.plot(freq[:round(len(freq) / 2)], abs(c[:round(len(c) / 2)]), 'r')
# plt.title('Freq')
# plt.xlabel("Freq/Hz")
# plt.show()
