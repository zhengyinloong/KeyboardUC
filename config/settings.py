# -*- coding: UTF-8 -*-
# settings.py in KeyboardUC
# zhengyinloong
# 2023/9/2

UI_WIDTH = 800
UI_HEIGHT = 600

PASSWORD = '123456'  # ubuntu

VENDOR_ID = 0x0d00  # GD32-USB_Keyboard / mouse VID
PRODUCT_ID = 0x0721  # GD32-USB_Keyboard / mouse PID

VENDOR_ID_CH341 = 0x1a86  # GD32-USB_Keyboard / I2C VID
PRODUCT_ID_CH341 = 0x5512  # GD32-USB_Keyboard / I2C PID

KEY_BOARD_CODES = {
    0x00: 'Reserved',
    0x01: 'ErrorRollOver',
    0x02: 'POSTFail',
    0x03: 'ErrorUndefined',
    0x04: 'A',
    0x05: 'B',
    0x06: 'C',
    0x07: 'D',
    0x08: 'E',
    0x09: 'F',
    0x0A: 'G',
    0x0B: 'H',
    0x0C: 'I',
    0x0D: 'J',
    0x0E: 'K',
    0x0F: 'L',
    0x10: 'M',
    0x11: 'N',
    0x12: 'O',
    0x13: 'P',
    0x14: 'Q',
    0x15: 'R',
    0x16: 'S',
    0x17: 'T',
    0x18: 'U',
    0x19: 'V',
    0x1A: 'W',
    0x1B: 'X',
    0x1C: 'Y',
    0x1D: 'Z',
    0x1E: '1 !',
    0x1F: '2 @',
    0x20: '3 #',
    0x21: '4 $',
    0x22: '5 %',
    0x23: '6 ^',
    0x24: '7 &',
    0x25: '8 *',
    0x26: '9 (',
    0x27: '0 )',
    0x28: 'Enter',
    0x29: 'Esc',
    0x2A: 'Backspace',
    0x2B: 'Tab',
    0x2C: 'Space',
    0x2D: '- _',
    0x2E: '= +',
    0x2F: '[ {',
    0x30: '] }',
    0x31: '\ |',
    0x32: 'NonUS# ~',
    0x33: '; :',
    0x34: '\' "',
    0x35: '` ~',
    0x36: ', <',
    0x37: '. >',
    0x38: '/ ?',
    0x39: 'CapsLock',
    0x3A: 'F1',
    0x3B: 'F2',
    0x3C: 'F3',
    0x3D: 'F4',
    0x3E: 'F5',
    0x3F: 'F6',
    0x40: 'F7',
    0x41: 'F8',
    0x42: 'F9',
    0x43: 'F10',
    0x44: 'F11',
    0x45: 'F12',
    0x46: 'PrintScreen',
    0x47: 'ScrollLock',
    0x48: 'Pause',
    0x49: 'Insert',
    0x4A: 'Home',
    0x4B: 'PageUp',
    0x4C: 'Delete',
    0x4D: 'End',
    0x4E: 'PageDown',
    0x4F: 'RightArrow',
    0x50: 'LeftArrow',
    0x51: 'DownArrow',
    0x52: 'UpArrow',
    0x53: 'NumLock',
    0x54: 'Keypad/',
    0x55: 'Keypad*',
    0x56: 'Keypad-',
    0x57: 'Keypad+',
    0x58: 'KeypadEnter',
    0x59: 'Keypad1',
    0x5A: 'Keypad2',
    0x5B: 'Keypad3',
    0x5C: 'Keypad4',
    0x5D: 'Keypad5',
    0x5E: 'Keypad6',
    0x5F: 'Keypad7',
    0x60: 'Keypad8',
    0x61: 'Keypad9',
    0x62: 'Keypad0',
    0x63: 'Keypad.',
    0x64: 'NonUS \ |',
    0x65: 'Application',
    0x66: 'Power',
    0x67: 'Keypad=',
    0x68: 'F13',
    0x69: 'F14',
    0x6A: 'F15',
    0x6B: 'F16',
    0x6C: 'F17',
    0x6D: 'F18',
    0x6E: 'F19',
    0x6F: 'F20',
    0x70: 'F21',
    0x71: 'F22',
    0x72: 'F23',
    0x73: 'F24',
    0x74: 'Execute',
    0x75: 'Help',
    0x76: 'Menu',
    0x77: 'Select',
    0x78: 'Stop',
    0x79: 'Again',
    0x7A: 'Undo',
    0x7B: 'Cut',
    0x7C: 'Copy',
    0x7D: 'Paste',
    0x7E: 'Find',
    0x7F: 'Mute',
    0x80: 'VolumeUp',
    0x81: 'VolumeDown',
    0x82: 'LockingCapsLock',
    0x83: 'LockingNumLock',
    0x84: 'LockingScrollLock',
    0x85: 'Keypad,',
    0x86: 'Keypad=AS400',
    0x87: 'International1',
    0x88: 'International2',
    0x89: 'International3',
    0x8A: 'International4',
    0x8B: 'International5',
    0x8C: 'International6',
    0x8D: 'International7',
    0x8E: 'International8',
    0x8F: 'International9',
    0x90: 'LANG1',
    0x91: 'LANG2',
    0x92: 'LANG3',
    0x93: 'LANG4',
    0x94: 'LANG5',
    0x95: 'LANG6',
    0x96: 'LANG7',
    0x97: 'LANG8',
    0x98: 'LANG9',
    0x99: 'AlternateErase',
    0x9A: 'SysReq/Attention',
    0x9B: 'Cancel',
    0x9C: 'Clear',
    0x9D: 'Prior',
    0x9E: 'Return',
    0x9F: 'Separator',
    0xA0: 'Out',
    0xA1: 'Oper',
    0xA2: 'Clear/Again',
    0xA3: 'CrSel/Props',
    0xA4: 'ExSel',
    0xE0: 'LeftControl',
    0xE1: 'LeftShift',
    0xE2: 'LeftAlt',
    0xE3: 'LeftGUI',
    0xE4: 'RightControl',
    0xE5: 'RightShift',
    0xE6: 'RightAlt',
    0xE7: 'RightGUI',
    0xFF: 'Undefined',
}
KEY_NAMES = ['Reserved', 'ErrorRollOver', 'POSTFail', 'ErrorUndefined', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
             'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1 !', '2 @', '3 #', '4 $', '5 %', '6 ^', '7 &', '8 *', '9 (', '0 )', 'Enter',
             'Esc', 'Backspace', 'Tab', 'Space', '- _', '= +', '[ {', '] }', '\\ |', 'NonUS# ~', '; :', '\' "', '` ~', ', <', '. >', '/ ?',
             'CapsLock', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'PrintScreen', 'ScrollLock', 'Pause', 'Insert',
             'Home', 'PageUp', 'Delete', 'End', 'PageDown', 'RightArrow', 'LeftArrow', 'DownArrow', 'UpArrow', 'NumLock', 'Keypad/', 'Keypad*',
             'Keypad-', 'Keypad+', 'KeypadEnter', 'Keypad1', 'Keypad2', 'Keypad3', 'Keypad4', 'Keypad5', 'Keypad6', 'Keypad7', 'Keypad8', 'Keypad9',
             'Keypad0', 'Keypad.', 'NonUS \\ |', 'Application', 'Power', 'Keypad=', 'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21',
             'F22', 'F23', 'F24', 'Execute', 'Help', 'Menu', 'Select', 'Stop', 'Again', 'Undo', 'Cut', 'Copy', 'Paste', 'Find', 'Mute', 'VolumeUp',
             'VolumeDown', 'LockingCapsLock', 'LockingNumLock', 'LockingScrollLock', 'Keypad,', 'Keypad=AS400', 'International1', 'International2',
             'International3', 'International4', 'International5', 'International6', 'International7', 'International8', 'International9', 'LANG1',
             'LANG2', 'LANG3', 'LANG4', 'LANG5', 'LANG6', 'LANG7', 'LANG8', 'LANG9', 'AlternateErase', 'SysReq/Attention', 'Cancel', 'Clear', 'Prior',
             'Return', 'Separator', 'Out', 'Oper', 'Clear/Again', 'CrSel/Props', 'ExSel', 'LeftControl', 'LeftShift', 'LeftAlt', 'LeftGUI',
             'RightControl', 'RightShift', 'RightAlt', 'RightGUI', 'Undefined']
KEY_BOARD_CODES_ = {'Reserved': 0, 'ErrorRollOver': 1, 'POSTFail': 2, 'ErrorUndefined': 3, 'A': 4, 'B': 5, 'C': 6, 'D': 7, 'E': 8, 'F': 9, 'G': 10,
                    'H': 11, 'I': 12, 'J': 13, 'K': 14, 'L': 15, 'M': 16, 'N': 17, 'O': 18, 'P': 19, 'Q': 20, 'R': 21, 'S': 22, 'T': 23, 'U': 24,
                    'V': 25, 'W': 26, 'X': 27, 'Y': 28, 'Z': 29, '1 !': 30, '2 @': 31, '3 #': 32, '4 $': 33, '5 %': 34, '6 ^': 35, '7 &': 36,
                    '8 *': 37, '9 (': 38, '0 )': 39, 'Enter': 40, 'Esc': 41, 'Backspace': 42, 'Tab': 43, 'Space': 44, '- _': 45, '= +': 46, '[ {': 47,
                    '] }': 48, '\\ |': 49, 'NonUS# ~': 50, '; :': 51, '\' "': 52, '` ~': 53, ', <': 54, '. >': 55, '/ ?': 56, 'CapsLock': 57,
                    'F1': 58, 'F2': 59, 'F3': 60, 'F4': 61, 'F5': 62, 'F6': 63, 'F7': 64, 'F8': 65, 'F9': 66, 'F10': 67, 'F11': 68, 'F12': 69,
                    'PrintScreen': 70, 'ScrollLock': 71, 'Pause': 72, 'Insert': 73, 'Home': 74, 'PageUp': 75, 'Delete': 76, 'End': 77, 'PageDown': 78,
                    'RightArrow': 79, 'LeftArrow': 80, 'DownArrow': 81, 'UpArrow': 82, 'NumLock': 83, 'Keypad/': 84, 'Keypad*': 85, 'Keypad-': 86,
                    'Keypad+': 87, 'KeypadEnter': 88, 'Keypad1': 89, 'Keypad2': 90, 'Keypad3': 91, 'Keypad4': 92, 'Keypad5': 93, 'Keypad6': 94,
                    'Keypad7': 95, 'Keypad8': 96, 'Keypad9': 97, 'Keypad0': 98, 'Keypad.': 99, 'NonUS \\ |': 100, 'Application': 101, 'Power': 102,
                    'Keypad=': 103, 'F13': 104, 'F14': 105, 'F15': 106, 'F16': 107, 'F17': 108, 'F18': 109, 'F19': 110, 'F20': 111, 'F21': 112,
                    'F22': 113, 'F23': 114, 'F24': 115, 'Execute': 116, 'Help': 117, 'Menu': 118, 'Select': 119, 'Stop': 120, 'Again': 121,
                    'Undo': 122, 'Cut': 123, 'Copy': 124, 'Paste': 125, 'Find': 126, 'Mute': 127, 'VolumeUp': 128, 'VolumeDown': 129,
                    'LockingCapsLock': 130, 'LockingNumLock': 131, 'LockingScrollLock': 132, 'Keypad,': 133, 'Keypad=AS400': 134,
                    'International1': 135, 'International2': 136, 'International3': 137, 'International4': 138, 'International5': 139,
                    'International6': 140, 'International7': 141, 'International8': 142, 'International9': 143, 'LANG1': 144, 'LANG2': 145,
                    'LANG3': 146, 'LANG4': 147, 'LANG5': 148, 'LANG6': 149, 'LANG7': 150, 'LANG8': 151, 'LANG9': 152, 'AlternateErase': 153,
                    'SysReq/Attention': 154, 'Cancel': 155, 'Clear': 156, 'Prior': 157, 'Return': 158, 'Separator': 159, 'Out': 160, 'Oper': 161,
                    'Clear/Again': 162, 'CrSel/Props': 163, 'ExSel': 164, 'LeftControl': 224, 'LeftShift': 225, 'LeftAlt': 226, 'LeftGUI': 227,
                    'RightControl': 228, 'RightShift': 229, 'RightAlt': 230, 'RightGUI': 231, 'Undefined': 255}
