import pyautogui
from tkinter import filedialog
from time import sleep

def autobot():

    # Display the dialog for browsing files.
    filename = filedialog.askopenfilename(
    filetypes=(
        ("Text files", "*.txt"),
        ("Python Files", ("*.py", "*.pyx")),
        ("All Files", "*.*")
    )
)
    if filename:
        try:
            with open(filename, 'r') as archive:
                txt = archive.readlines()
                for line in txt:
                    line = line.split('|')
                    if line[0] == 'kb':
                        rec_text = line[1]
                        pyautogui.doubleClick(duration=0.5)
                        pyautogui.hotkey('delete')
                        pyautogui.hotkey('ctrl', 'a')
                        pyautogui.hotkey('delete')
                        pyautogui.write(rec_text)
                    if line[0] == 'ms':
                        x = line[1]
                        y = line[2]
                        pyautogui.click(int(x), int(y), duration=0.05)
                    if line[0] == 'msr':
                        x = line[1]
                        y = line[2]
                        pyautogui.rightClick(int(x), int(y), duration=0.05)

        except Exception:
            print("Erro aqui: final")
            print(Exception)
    else:
        print("No file selected.")