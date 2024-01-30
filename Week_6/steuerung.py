import pyautogui
import webbrowser
import time

def open_browser(url):
    webbrowser.open(url)
    
# utils.py
import pyautogui
import webbrowser
import time

def open_browser(url):
    webbrowser.open(url)

def click_at_position(x, y, duration=0.5):
    pyautogui.moveTo(x, y, duration=duration)
    pyautogui.click()

    




