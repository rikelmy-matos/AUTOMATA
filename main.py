from auto import autobot
from PIL import Image
from tkinter import filedialog
import os
import customtkinter
import mouse as ms


#pip install -r requirements.txt
#pip unistall -r -Y requirements.txt

# open window/config
root = customtkinter.CTk()
root.iconbitmap("favicon.ico")

w = 300 # width for the Tk root
h = 280 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/1.1) - (w/1.8)
y = (hs/1.1) - (h/1)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#root.resizable(width=0, height=0) #Don't allow resizing in the x or y direction
root.resizable(False, False)
root.title("Automata")

#function that receive the input and write into the archive(used in button2 | Keyboard input)
def receive_text():
    try:
        text_box = textbox.get()
        if text_box !='':

            try:
                with open(f'choosepy/choose.txt', 'r') as archive:
                    name_archive = archive.read()
                    archive.close()
            except Exception:
                print(Exception)

            try:
                with open(f'{name_archive}', 'a') as archive:
                    archive.write(f'{"kb"}|{"".join(text_box)}|{"null"}'+"\n")
                archive.close()
                
            except Exception:
                print(Exception)
        else:
            print("Write something...")
    except Exception:
                print(Exception)

# function that get the mouse coordinates
def get_mouse():
    try:
        #when is left is pressed
        ms.wait('left')
        ms.wait('left')
        #return the coordinate position
        x, y = ms.get_position()
        try:
            with open(f'choosepy/choose.txt', 'r') as archive:
                name_archive = archive.read()
                archive.close()
        except Exception:
            print(Exception)

        try:
            with open(f'{name_archive}', 'a') as archive:
                archive.write(f'{"ms"}|{x}|{y}\n')
                archive.close()
        except Exception:
            print(Exception)


    except Exception:
        print(Exception)

# function that get the mouse coordinates
def get_mouse_right():
    try:
        #when is left is pressed
        ms.wait('right')
        ms.wait('right')
        #return the coordinate position
        x, y = ms.get_position()
        try:
            with open(f'choosepy/choose.txt', 'r') as archive:
                name_archive = archive.read()
                archive.close()
                
        except Exception:
            print(Exception)

        try:
            with open(f'{name_archive}', 'a') as archive:
                archive.write(f'{"msr"}|{x}|{y}\n')
                archive.close()
        except Exception:
            print(Exception)
    except Exception:
        print(Exception)

#function that create an archive
def create_archive():

    try:
        archive_name = entry1.get()
        if archive_name != "":
            FileName = str("autopy/" + archive_name + ".txt")
            with open(FileName,"w"):
                pass
        else:
            print("Write the name!")
    except Exception:
        print(Exception)

#function that delete an archive
def delete_archive():

# Display the dialog for browsing files.
    filename = filedialog.askopenfilename(
    filetypes=(
        ("Text files", "*.txt"),
        ("Python Files", ("*.py", "*.pyx")),
        ("All Files", "*.*")
    )
)
    # Remove the file
    # 'file.txt'

    if filename !='':
        os.remove(filename)
    else:
        print("No file selected.")

#function that choose and save an archive path
def choose_archive():

    filename = filedialog.askopenfilename()
    if filename !='':
        with open("choosepy/choose.txt", 'w') as archive:
            archive.write(filename)
    else:
        print("No file selected.")
    

button_mode = True
def customize():

    global button_mode
    if button_mode:
        button_toogle.configure(image=button_image_off)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark_blue.json")
        root.config(bg="black", bd=0)
        button_mode = False

    else:
        button_toogle.configure(image=button_image_on)
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark_blue.json")
        root.config(bg="white", bd=0)
        button_mode = True

button_visible = True
def see():

    global button_visible
    if button_visible:
        button_see.configure(image=button_see_off)
        root.call('wm', 'attributes', '.', '-topmost', True)
        root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', True)
        button_visible = False

    else:
        button_see.configure(image=button_see_on)
        # the window will stay in the principal layer(in front)
        root.call('wm', 'attributes', '.', '-topmost', False)
        root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)
        button_visible = True

#frame that will contain the button entry and execute
entryframe = customtkinter.CTkFrame(root)
entryframe.pack(pady=2)
#button create
entry1 = customtkinter.CTkEntry(master=entryframe, border_color="black", width=175)
button_create = customtkinter.CTkButton(master=entryframe,border_color="black", width=20, text="Create file", command=create_archive)
button_create.pack(pady=2, padx=3, side='right', anchor='e', expand=True)
entry1.pack(pady=2, padx=3, side='left', anchor='w', expand=True)

#frame that will contain the button entry and execute
entryframe2 = customtkinter.CTkFrame(root)
entryframe2.pack(pady=2)
#button delete
button_delete = customtkinter.CTkButton(master=entryframe2,border_color="black", width=20, text="Delete file", command=delete_archive)
button_delete.pack(pady=2, padx=2, side='right', anchor='e', expand=True)

#button choose
button_choose = customtkinter.CTkButton(master=entryframe2,border_color="black", text="Choose file", command=choose_archive)
button_choose.pack(pady=2, padx=2, side='left', anchor='w', expand=True)


#frame that will contain the button entry and execute
entryframe3 = customtkinter.CTkFrame(root)
entryframe3.pack(pady=2)

#button save mouse input
button_left = customtkinter.CTkButton(master=entryframe3, border_color="black", text="Save mouse(left)", command=get_mouse)
button_left.pack(pady=2, padx=2, side='top', anchor='s', expand=True)


#button save mouse input
button_right = customtkinter.CTkButton(master=entryframe3, border_color="black", text="Save mouse(right)", command=get_mouse_right)
button_right.pack(pady=2, padx=2, side='top', anchor='s', expand=True)


#frame that will contain the button entry and execute
entryframe4 = customtkinter.CTkFrame(root)
entryframe4.pack(pady=2)
#button save keyboard input
textbox = customtkinter.CTkEntry(master=entryframe4, width=175, border_color="black")
button_keyboard = customtkinter.CTkButton(master=entryframe4, border_color="black", width=20, text="Save keyboard", command=receive_text)
textbox.pack(pady=2, padx=3, side='bottom', anchor='s', expand=True)
button_keyboard.pack(pady=2, padx=3, side='bottom', anchor='s', expand=True)


#frame that will contain the button create and execute
buttonframe = customtkinter.CTkFrame(root)
buttonframe.pack(pady=2)


#button execute
button_execute = customtkinter.CTkButton(master=buttonframe,border_color="black", width=20, text="Execute file", command=autobot, fg_color="lightgreen", hover_color="green", text_color="black")
button_execute.pack(pady=2, padx=60, side='right', anchor='e', expand=True)


#images
button_image_on = customtkinter.CTkImage(Image.open("img/light.png"), size=(50,22))
button_image_off = customtkinter.CTkImage(Image.open("img/dark.png"), size=(50,22))
button_see_on = customtkinter.CTkImage(Image.open("img/button-on.png"), size=(45,18))
button_see_off = customtkinter.CTkImage(Image.open("img/button-off.png"), size=(45,18))

#button that change the theme(dark/light)
button_toogle = customtkinter.CTkButton(master=buttonframe, fg_color='transparent', bg_color='transparent', border_width=0, hover='transparent', image=button_image_on, text='', command=customize)
button_toogle.pack(pady=2, side='left', anchor='w', expand=True)

#frame that will contain the button create and execute
buttonframe2 = customtkinter.CTkFrame(root)
buttonframe2.pack(pady=2, side="right")

#button see and unsee(stay open) don't
button_see = customtkinter.CTkButton(master=buttonframe2, width=8, height=5, fg_color='transparent', bg_color='transparent', border_width=0, hover='transparent', image=button_see_on, text='', command=see)
button_see.pack(pady=2, side='right', anchor='e', expand=True)

# infinit loop the window
root.mainloop()