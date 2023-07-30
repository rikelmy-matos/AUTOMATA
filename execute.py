import pyautogui
from tkinter import filedialog

#function that execute your file
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
                        vel = float(line[2])
                        pyautogui.doubleClick(duration=vel)
                        pyautogui.hotkey('delete')
                        pyautogui.hotkey('ctrl', 'a')
                        pyautogui.hotkey('delete')
                        pyautogui.write(rec_text)
                        
                    if line[0] == 'ms':
                        var = 0
                        x = line[1]
                        y = line[2]
                        clicks = line[3]
                        vel = float(line[4])
                        while(var < int(clicks)):
                            pyautogui.click(int(x), int(y), duration=vel)
                            var+=1

                    if line[0] == 'msr':
                        x = line[1]
                        y = line[2]
                        vel = float(line[3])
                        pyautogui.rightClick(int(x), int(y), duration=vel)

                    
                    if line[0] == 'hk':
                        hotkey_1 = line[1]
                        hotkey_2 = line[2]
                        vel = float(line[3])
                        pyautogui.hotkey(hotkey_1, hotkey_2, duration=vel)
                    
        except Exception:
            print(Exception)
    else:
        print("No file selected.")