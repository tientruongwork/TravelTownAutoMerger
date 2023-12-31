import win32api, win32gui, win32con
from init_app import child_app
import time


def dragAndDrop(source, destination):
    win32gui.SendMessage(
        child_app,
        win32con.WM_LBUTTONDOWN,
        win32con.MK_LBUTTON,
        win32api.MAKELONG(source[0], source[1]),
    )
    time.sleep(0.1)
    win32gui.SendMessage(
        child_app,
        win32con.WM_LBUTTONDOWN,
        win32con.MK_LBUTTON,
        win32api.MAKELONG(destination[0], destination[1]),
    )
    time.sleep(0.1)
    win32gui.SendMessage(
        child_app,
        win32con.WM_LBUTTONUP,
        win32con.MK_LBUTTON,
        win32api.MAKELONG(destination[0], destination[1]),
    )
    time.sleep(0.1)


def click(destination):
    win32gui.SendMessage(
        child_app,
        win32con.WM_LBUTTONDOWN,
        win32con.MK_LBUTTON,
        win32api.MAKELONG(
            destination[0],
            destination[1],
        ),
    )
    win32gui.SendMessage(
        child_app,
        win32con.WM_LBUTTONUP,
        win32con.MK_LBUTTON,
        win32api.MAKELONG(
            destination[0],
            destination[1],
        ),
    )


def doubleClick(destination):
    click(destination)
    time.sleep(0.1)
    click(destination)
