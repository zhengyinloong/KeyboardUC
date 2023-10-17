# -*- coding:utf-8 -*-
# test5.py in KeyboardUC
# zhengyinloong
# 2023/10/14

KEY_BOARD_CODES = {
    0x1: "MOUSE LEFT",
    0x2: "MOUSE RIGHT",
    0x3: "CANCEL",
    0x4: "MOUSE MID",
    # 控制键键码值
    0x8: "BACKSPACE",
    0x9: "TAB",
    0xC: "CLEAR",
    0xD: "ENTER",
    0x10: "SHIFT",
    0x11: "CTRL",
    0x12: "ALT",
    0x13: "PAUSE",
    0x14: "CAPSLOCK",
    0x1B: "ESC",
    0x20: "SPACE",
    0x21: "PAGE UP",
    0x22: "PAGE DOWN",
    0x23: "END",
    0x24: "HOME",
    0x25: "LEFT ARROW",
    0x26: "UP ARROW",
    0x27: "RIGHT ARROW",
    0x28: "DOWN ARROW",
    0x29: "SELECT",
    0x2A: "PRINT SCREEN",
    0x2B: "EXECUTE",
    0x2C: "SNAPSHOT",
    0x2D: "INSERT",
    0x2E: "DELETE",
    0x2F: "HELP",
    0x90: "NUM LOCK",

    186: ";:",
    187: "=+",
    188: ",<",
    189: "-_",
    190: ".>",
    191: "/?",
    192: "`~",
    219: "[{",
    220: "/|",
    221: "]}",
    222: "'",

    # 字母和数字键码值
    65: "A",
    66: "B",
    67: "C",
    68: "D",
    69: "E",
    70: "F",
    71: "G",
    72: "H",
    73: "I",
    74: "J",
    75: "K",
    76: "L",
    77: "M",
    78: "N",
    79: "O",
    80: "P",
    81: "Q",
    82: "R",
    83: "S",
    84: "T",
    85: "U",
    86: "V",
    87: "W",
    88: "X",
    89: "Y",
    90: "Z",
    48: "0",
    49: "1",
    50: "2",
    51: "3",
    52: "4",
    53: "5",
    54: "6",
    55: "7",
    56: "8",
    57: "9",
    0x60: "NUM0",
    0x61: "NUM1",
    0x62: "NUM2",
    0x63: "NUM3",
    0x64: "NUM4",
    0x65: "NUM5",
    0x66: "NUM6",
    0x67: "NUM7",
    0x68: "NUM8",
    0x69: "NUM9",
    0x6A: "*",
    0x6B: "+",
    0x6C: "NUM ENTER",
    0x6D: "–",
    0x6E: ".",
    0x6F: "/",
    # 功能键键码值 F1～F16
    0x70: "F1",
    0x71: "F2",
    0x72: "F3",
    0x73: "F4",
    0x74: "F5",
    0x75: "F6",
    0x76: "F7",
    0x77: "F8",
    0x78: "F9",
    0x79: "F10",
    0x7A: "F11",
    0x7B: "F12",
    0x7C: "F13",
    0x7D: "F14",
    0x7E: "F15",
    0x7F: "F16"}
KEY_NAMES = ['MOUSE LEFT', 'MOUSE RIGHT', 'CANCEL', 'MOUSE MID', 'BACKSPACE', 'TAB', 'CLEAR', 'ENTER', 'SHIFT', 'CTRL',
             'ALT', 'PAUSE', 'CAPSLOCK', 'ESC', 'SPACE', 'PAGE UP', 'PAGE DOWN', 'END', 'HOME', 'LEFT ARROW',
             'UP ARROW', 'RIGHT ARROW', 'DOWN ARROW', 'SELECT', 'PRINT SCREEN', 'EXECUTE', 'SNAPSHOT', 'INSERT',
             'DELETE', 'HELP', 'NUM LOCK', ';:', '=+', ',<', '-_', '.>', '/?', '`~', '[{', '/|', ']}', "'", 'A', 'B',
             'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'NUM0', 'NUM1', 'NUM2', 'NUM3', 'NUM4',
             'NUM5', 'NUM6', 'NUM7', 'NUM8', 'NUM9', '*', '+', 'NUM ENTER', '–', '.', '/', 'F1', 'F2', 'F3', 'F4', 'F5',
             'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16']

_KEY_BOARD_CODES = {'MOUSE LEFT': 1, 'MOUSE RIGHT': 2, 'CANCEL': 3, 'MOUSE MID': 4, 'BACKSPACE': 8, 'TAB': 9, 'CLEAR': 12,
                    'ENTER': 13, 'SHIFT': 16, 'CTRL': 17, 'ALT': 18, 'PAUSE': 19, 'CAPSLOCK': 20, 'ESC': 27, 'SPACE': 32,
                    'PAGE UP': 33, 'PAGE DOWN': 34, 'END': 35, 'HOME': 36, 'LEFT ARROW': 37, 'UP ARROW': 38, 'RIGHT ARROW': 39,
                    'DOWN ARROW': 40, 'SELECT': 41, 'PRINT SCREEN': 42, 'EXECUTE': 43, 'SNAPSHOT': 44, 'INSERT': 45, 'DELETE': 46,
                    'HELP': 47, 'NUM LOCK': 144, ';:': 186, '=+': 187, ',<': 188, '-_': 189, '.>': 190, '/?': 191, '`~': 192,
                    '[{': 219, '/|': 220, ']}': 221, "'": 222, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72,
                    'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84,
                    'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53,
                    '6': 54, '7': 55, '8': 56, '9': 57, 'NUM0': 96, 'NUM1': 97, 'NUM2': 98, 'NUM3': 99, 'NUM4': 100, 'NUM5': 101,
                    'NUM6': 102, 'NUM7': 103, 'NUM8': 104, 'NUM9': 105, '*': 106, '+': 107, 'NUM ENTER': 108, '–': 109, '.': 110,
                    '/': 111, 'F1': 112, 'F2': 113, 'F3': 114, 'F4': 115, 'F5': 116, 'F6': 117, 'F7': 118, 'F8': 119, 'F9': 120,
                    'F10': 121, 'F11': 122, 'F12': 123, 'F13': 124, 'F14': 125, 'F15': 126, 'F16': 127}

KEY_NAMES = []
for n in KEY_BOARD_CODES.values():
    KEY_NAMES.append(n)
_KEY_BOARD_CODES = {}
for it in KEY_BOARD_CODES.items():
    # print(it)
    _KEY_BOARD_CODES[it[1]] = it[0]
print(KEY_NAMES)
print(_KEY_BOARD_CODES)

print(len(KEY_NAMES))
print(len(_KEY_BOARD_CODES))
print(len(KEY_BOARD_CODES))
