# -*- coding:utf-8 -*-
# test6.py in KeyboardUC
# zhengyinloong
# 2023/10/17

import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import wave

chunk = 1024  # 缓冲区大小
format = pyaudio.paInt16  # 采样位数
channels = 1  # 声道数
framerate = 44100  # 采样率
sampwidth = 2


def save_wave_file(filename, data):  # save the date to the wav file
    wf = wave.open(filename, 'wb')  # 二进制写入模式
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)  # 两个字节16位
    wf.setframerate(framerate)  # 帧速率
    wf.writeframes(b"".join(data))  # 把数据加进去，就会存到硬盘上去wf.writeframes(b"".join(data))
    wf.close()


wave_data = []
data = np.zeros(chunk, dtype=np.int16)

p = pyaudio.PyAudio()

stream = p.open(format=format,
                channels=channels,
                rate=framerate,
                input=True,
                frames_per_buffer=chunk)

fig, ax = plt.subplots()
x = np.arange(0, 2 * chunk, 2)
line, = ax.plot(x, np.random.rand(chunk), 'r')
ax.set_ylim(0, 100)
ax.set_xlim(0, chunk)
bar = ax.bar(1, 0, width=100)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
volume = 0
input_flag = True


def handle_close(event):
    global input_flag
    input_flag = False
    plt.close()
    stream.stop_stream()
    stream.close()
    p.terminate()
    # sys.exit(0)


fig.canvas.mpl_connect('close_event', handle_close)
while input_flag:
    data = stream.read(chunk)
    wave_data.append(data)
    data_int = np.frombuffer(data, dtype=np.int16)
    volume = max(data_int) * 100 / 32768
    bar[0].set_height(volume)
    _fft = np.fft.fft(data_int)
    # print(len(_fft))
    line.set_ydata(_fft)

    fig.canvas.draw()
    fig.canvas.flush_events()
    fig.show()

save_wave_file('test.wav', wave_data)

plt.close()
stream.stop_stream()
stream.close()
p.terminate()
