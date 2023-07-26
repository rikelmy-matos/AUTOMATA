------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# "Autobot" created using Python3 and Customtkinter

# This project saves your inputs (mouse and keyboard text) and saves them in a.txt file, so you can read that file and perform the action repeatedly...

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# HOW TO USE:
1 - Install "requirements.txt" -> run in your terminal "pip install -r requirements.txt"

2 - Run the file "main.py"

3 - Write the name of the file you want to create -> click on (Create file button) -> the file will be created in "autopy folder"

4 - Click on (Choose file) -> choose the file you created -> a file will be created with the path of the file inside the "controlpy folder" -> this folder is for control

5 - When choosing your file, just click on (save mouse) -> (when selecting just click on something/somewhere) -> it will save the coordinate and record it in the file you created

6 - When you choose your file just write something in the text input and click on (save keyboard) -> it will save the string and write in the file you created

# AFTER:
7 - When saving all the steps you want, just click on (Execute file) and choose the file you created in "autopy folder"

8 - If you want to create another file just repeat (create -> choose ->Save(mouse | keyboard) )

# .exe:
9 - Run in your terminal "pyinstaller -w -F -i "{path}/favicon.ico" "{path}/main.py" -> To find the executable file, open the dist folder, and take the file.exe and place it in the same path as main.py
