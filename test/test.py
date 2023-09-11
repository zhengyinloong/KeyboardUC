# -*- coding: utf-8 -*-
from array import array

# b = b"Hello, World!"
#
# b1 = 'Hello, World!'.encode()
# print(b,b1.decode())

a = array('B', [0, 0, 0, 255])
'''
鼠标发送给PC的数据每次4个字节
BYTE1 BYTE2 BYTE3 BYTE4
定义分别是：
BYTE1 --
       |--bit7:   1   表示   Y   坐标的变化量超出－256   ~   255的范围,0表示没有溢出
       |--bit6:   1   表示   X   坐标的变化量超出－256   ~   255的范围，0表示没有溢出
       |--bit5:   Y   坐标变化的符号位，1表示负数，即鼠标向下移动
       |--bit4:   X   坐标变化的符号位，1表示负数，即鼠标向左移动
       |--bit3:     恒为1
       |--bit2:     1表示中键按下
       |--bit1:     1表示右键按下
       |--bit0:     1表示左键按下
BYTE2 -- X坐标变化量，与byte的bit4组成9位符号数,负数表示向左移，正数表右移。用补码表示变化量
BYTE3 -- Y坐标变化量，与byte的bit5组成9位符号数，负数表示向下移，正数表上移。用补码表示变化量
BYTE4 -- 滚轮变化。
'''
useful = list(a)
def parse_mouse_packet(packet):
    byte1 = packet[0]
    byte2 = packet[1]
    byte3 = packet[2]
    byte4 = packet[3]

    x_overflow = (byte1 & 0b10000000) >> 7
    y_overflow = (byte1 & 0b01000000) >> 6
    y_negative = (byte1 & 0b00100000) >> 5
    x_negative = (byte1 & 0b00010000) >> 4
    middle_btn_pressed = (byte1 & 0b00000100) >> 2
    right_btn_pressed = (byte1 & 0b00000010) >> 1
    left_btn_pressed = byte1 & 0b00000001

    # Calculate X coordinate change
    x_change = byte2 if not x_negative else -(256 - byte2)

    # Calculate Y coordinate change
    y_change = byte3 if not y_negative else -(256 - byte3)

    # Get scroll wheel change
    scroll_change = byte4

    return {
        'x_overflow': bool(x_overflow),
        'y_overflow': bool(y_overflow),
        'x_negative': bool(x_negative),
        'y_negative': bool(y_negative),
        'middle_btn_pressed': bool(middle_btn_pressed),
        'right_btn_pressed': bool(right_btn_pressed),
        'left_btn_pressed': bool(left_btn_pressed),
        'x_change': x_change,
        'y_change': y_change,
        'scroll_change': scroll_change
    }

print(parse_mouse_packet(useful))

