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

## TESTS

+ usb test:
  + mouse test
    + test ![test](resources/usbtest.png)
      + left button ![mouse test left button](resources/usb_mouse_test_left_btn.png)
      + scroll ![mouse test scroll](resources/receive_mouse_data.png)
  + keyboard test
    + interface ![keyboard interface](resources/keyboradInterface.png)