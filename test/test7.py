# -*- coding:utf-8 -*-
# test7.py in KeyboardUC
# zhengyinloong
# 2023/11/2

# 播放wav音频

import wave
import sys
import pyaudio
import matplotlib.pyplot as plt
import numpy as np

# with语句块保证文件在使用结束后会被正确地关闭
with wave.open('/home/loong/KeyboardUC/resources/audio/test.wav', 'rb') as wf:
    # 实例化一个PyAudio对象，并初始化PortAudio系统资源
    p = pyaudio.PyAudio()

    # 获取wav文件参数元组(nchannels, sampwidth, framerate, nframes, comptype, compname)
    params = wf.getparams()

    # 打开音频流
    stream = p.open(channels=params[0],
                    format=params[1],
                    rate=params[2],
                    output=True)
    chunk = 1024
    fig, ax = plt.subplots()
    x = np.arange(0, 2 * chunk, 2)
    line, = ax.plot(x, np.random.rand(chunk), 'r')
    ax.set_ylim(0, 100)
    ax.set_xlim(0, chunk)
    bar = ax.bar(1, 0, width=100)
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')

    # 每次读取1024字节大小的音频数据到音频流中播放，直到读完全部音频数据
    while True:
        data = wf.readframes(1024)
        if not data:
            break
        stream.write(data)
        data_int = np.frombuffer(data, dtype=np.int16)
        volume = max(data_int) * 100 / 32768
        bar[0].set_height(volume)
        _fft = np.fft.fft(data_int)
        # print(len(_fft))
        line.set_ydata(_fft)

        fig.canvas.draw()
        fig.canvas.flush_events()
        fig.show()

    # 关闭音频流，释放PortAudio系统资源
    stream.close()

    # 终止PyAudio对象，释放占用的系统资源
    p.terminate()

# 退出程序
sys.exit(0)
