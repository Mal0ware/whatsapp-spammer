import pyautogui 
import webbrowser as wb
import time
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' # Make sure to add your google chrome's exe file path! you can choose a different web browser.
wb.get(chrome_path).open("web.whatsapp.com")
time.sleep(15) # You have 15 seconds to open a chat before it starts spamming
while True: # while True = loop
    pyautogui.typewrite("Your message here")
    pyautogui.press("enter")
    
# https://github.com/DiabloTheDev