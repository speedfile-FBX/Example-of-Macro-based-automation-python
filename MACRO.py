import pygetwindow as gw
import sys
import os
import time
import subprocess
import pyautogui
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "ip.txt")
open(file_path, "w").close()

os.startfile("cmd.exe")
os.startfile(file_path)
time.sleep(0.70)
windows = (
    gw.getWindowsWithTitle("Windows Command Processor")
    + gw.getWindowsWithTitle("C:\\Windows\\System32\\cmd.exe")
)
if windows:
    window = windows[0]
    window.activate()
    pyautogui.write("TEST")
    time.sleep(0.10)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    windows = gw.getWindowsWithTitle("ip.txt - Notepad")
    window = windows[0]
    window.activate()
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("ctrl", "s")
    subprocess.run(["taskkill", "/IM", "notepad.exe", "/F"])
    subprocess.run(["taskkill", "/IM", "cmd.exe", "/F"])
    sys.exit()
else:
    print("how did you do this man?")
    time.sleep(3)
    sys.exit()