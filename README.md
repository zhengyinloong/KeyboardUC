# KeyboardUC

## BEFORE IT

```bash
sudo nautilus 50-myusbkeyboard.rules /etc/udev/rules.d
# This will pop up two windows, source and destination. 
# Copy the file you want to move in the source window, then paste it in the destination window.
# Once successful, close them，done
```

```bash
sudo adduser <username> plugdev
```

## Bluetooth By Terminal

```bash
sudo bluetoothctl  # input password and press enter
```

```
menu gatt
#list-attributes 
select-attribute /org/bluez/hci0/dev_34_08_E1_1C_44_9D/service0054/char0055
write 0xff
```

## I2C By CH341T USB-I2C

|    function    | Data1 | Data2 | Data                               |
|:--------------:|:------|-------|------------------------------------|
|    I2C init    | -     | -     | aa6000                             |
|   Mousescan    | 00    | 1     | aa4a4a74827200748173c4c07500       |
|  Keyboardscan  | 01    | 1     | aa4a4a74827201748173c8c07500       |
|     Light      | 02    | 1     | aa4a4a74837202ff748173c0c07500     |
| Keyboardlayout | 04    | 1     | aa4a4a74857204000005748173c1c07500 |

## TESTS

+ usb test:
    + mouse test
        + test ![test](resources/imgs/usbtest.png)
            + left button ![mouse test left button](resources/imgs/usb_mouse_test_left_btn.png)
            + scroll ![mouse test scroll](resources/imgs/receive_mouse_data.png)
    + keyboard test
        + interface ![keyboard interface](resources/imgs/keyboradInterface.png)
