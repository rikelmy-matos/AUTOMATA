import os
import mouse as ms
import customtkinter
import pyautogui
from datetime import datetime
from PIL import Image
from tkinter import filedialog
from time import sleep

########################################################## CONFIG ####################################################################################
#pip install -r requirements.txt
#pip unistall -r -Y requirements.txt

# open window/config
app = customtkinter.CTk()
app.iconbitmap("favicon.ico")
w = 670 # width for the Tk root
h = 420 # height for the Tk root
# get screen width and height
ws = app.winfo_screenwidth() # width of the screen
hs = app.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/1.1) - (w/1.2)
y = (hs/1.1) - (h/1)

customtkinter.set_default_color_theme("dark_blue.json")
# set the dimensions of the screen 
# and where it is placed
app.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
#Don't allow resizing in the x or y direction
app.resizable(False, False)
#Title
app.title("Automata")

#log_varible control
text_log = ""
#font
font_tuple = ("Roboto", 20, "bold")
font_text = ("Roboto", 13, "normal")
########################################################## FUNCTIONS ##################################################################################
#function that write the user log(inputs)
def logs(text_value):
    log_label.insert("0.0", text_value)

#function that create an archive
def create_archive():

    try:
        archive_name = entry_name_file.get()
        if archive_name != "":
            FileName = str("autopy/" + archive_name + ".txt")
            with open(FileName,"w"):
                data_e_hora_atuais = datetime.now()
                hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
                text_log = f'{hora_em_texto} - "created: ", {archive_name}\n'
                logs(text_log)
            
        else:
            print("Write the name!")
    except Exception:
        print(Exception)

#function that choose and save an archive path
def choose_archive():

    filename = filedialog.askopenfilename()
    if filename !='':
        with open("controlpy/choose.txt", 'w') as archive:
            archive.write(filename)
            filename = filename.split("/")
            filename = filename[-1]
            data_e_hora_atuais = datetime.now()
            hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            text_log = f'{hora_em_texto} - "selected: ", {filename}\n'
            logs(text_log)
    else:
        print("No file selected.")

#function that delete an file
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
        filename = filename.split("/")
        filename = filename[-1]
        data_e_hora_atuais = datetime.now()
        hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
        text_log = f'{hora_em_texto} - "deleted: ", {filename}\n'
        logs(text_log)
    else:
        print("No file selected.")

#function that saves the clicks
def slider_click():
    current_value = int(slider_clicks.get())
    try:
        with open("controlpy/clicks.txt", 'w') as archive:
            archive.write(f'{str(current_value)}|{None}')
            data_e_hora_atuais = datetime.now()
            hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            text_log = f'{hora_em_texto} - "clicks : ", {current_value}\n'
            logs(text_log)
    except Exception:
        print(Exception)

#function that saves the clicks
def slider_vel():
    current_value = float(slider_velocity.get())
    current_value = f'{current_value:.2f}'
    try:
        with open("controlpy/vel.txt", 'w') as archive:
            archive.write(f'{current_value}|{None}')
            data_e_hora_atuais = datetime.now()
            hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            text_log = f'{hora_em_texto} - "velocity : ", {current_value}\n'
            logs(text_log)

    except Exception:
        print(Exception)

# function that get the mouse coordinates
def get_mouse_left():
    try:
        #when is left is pressed
        ms.wait('left')
        ms.wait('left')
        #return the coordinate position
        x, y = ms.get_position()
        try:
            with open(f'controlpy/choose.txt', 'r') as archive:
                name_archive = archive.read()
                archive.close()
        except Exception:
            print(Exception)

        try:
            with open("controlpy/clicks.txt", 'r') as archive:
                clicks = archive.read()
                clicks = clicks.split("|")
                clicks = clicks[0]

            with open("controlpy/vel.txt", 'r') as archive:
                vel = archive.read()
                vel = vel.split("|")
                vel = vel[0]

            with open(f'{name_archive}', 'a') as archive:
                archive.write(f'{"ms"}|{x}|{y}|{clicks}|{vel}|{None}\n')
                data_e_hora_atuais = datetime.now()
                hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
                text_log = f'{hora_em_texto} - "mouse(left): ", set{x,y}\n'
                logs(text_log)
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
            with open(f'controlpy/choose.txt', 'r') as archive:
                name_archive = archive.read()
                archive.close()
                
        except Exception:
            print(Exception)

        try:
            with open("controlpy/vel.txt", 'r') as archive:
                vel = archive.read()
                vel = vel.split("|")
                vel = vel[0]
            with open(f'{name_archive}', 'a') as archive:
                archive.write(f'{"msr"}|{x}|{y}|{vel}|{None}\n')
                data_e_hora_atuais = datetime.now()
                hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
                text_log = f'{hora_em_texto} - "mouse(right): ", set{x,y}\n'
                logs(text_log)
                archive.close()
        except Exception:
            print(Exception)
    except Exception:
        print(Exception)

#function that receive the input and write into the archive(used in button2 | Keyboard input)
def receive_text():
    try:
        text_box = textbox.get()
        if text_box !='':

            try:
                with open(f'controlpy/choose.txt', 'r') as archive:
                    name_archive = archive.read()
                    archive.close()
            except Exception:
                print(Exception)

            try:
                with open("controlpy/vel.txt", 'r') as archive:
                    vel = archive.read()
                    vel = vel.split("|")
                    vel = vel[0]
                with open(f'{name_archive}', 'a') as archive:
                    archive.write(f'{"kb"}|{"".join(text_box)}|{vel}|{None}'+"\n")
                    data_e_hora_atuais = datetime.now()
                    hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
                    text_log = f'{hora_em_texto} - "keyboard: ", {text_box}\n'
                    logs(text_log)
                archive.close()
                
            except Exception:
                print(Exception)
        else:
            print("Write something...")
    except Exception:
                print(Exception)

#function that save the hotkey ctrl + a
def funct_select_all():

    try:
        with open(f'controlpy/choose.txt', 'r') as archive:
            name_archive = archive.read()
            archive.close()
    except Exception:
        print(Exception)

    try:
        with open("controlpy/vel.txt", 'r') as archive:
            vel = archive.read()
            vel = vel.split("|")
            vel = vel[0]
        with open(f'{name_archive}', 'a') as archive:
            archive.write(f'{"hk"}|{"ctrl"}|{"a"}|{vel}|{None}'+"\n")
            data_e_hora_atuais = datetime.now()
            hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            text_log = f'{hora_em_texto} - "hotkey: ", "ctrl + a"\n'
            logs(text_log)
            archive.close()
                
    except Exception:
        print(Exception)

#function that save the hotkey ctrl + c
def funct_copy():

    try:
        with open(f'controlpy/choose.txt', 'r') as archive:
            name_archive = archive.read()
            archive.close()
    except Exception:
        print(Exception)

    try:
        with open("controlpy/vel.txt", 'r') as archive:
            vel = archive.read()
            vel = vel.split("|")
            vel = vel[0]
        with open(f'{name_archive}', 'a') as archive:
            archive.write(f'{"hk"}|{"ctrl"}|{"c"}|{vel}|{None}'+"\n")
            data_e_hora_atuais = datetime.now()
            hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            text_log = f'{hora_em_texto} - "hotkey: ", "ctrl + c"\n'
            logs(text_log)
            archive.close()
                
    except Exception:
        print(Exception)

#function that save the hotkey ctrl + v
def funct_paste():

    try:
        with open(f'controlpy/choose.txt', 'r') as archive:
            name_archive = archive.read()
            archive.close()
    except Exception:
        print(Exception)

    try:
        with open("controlpy/vel.txt", 'r') as archive:
            vel = archive.read()
            vel = vel.split("|")
            vel = vel[0]
        with open(f'{name_archive}', 'a') as archive:
            archive.write(f'{"hk"}|{"ctrl"}|{"v"}|{vel}|{None}'+"\n")
            data_e_hora_atuais = datetime.now()
            hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
            text_log = f'{hora_em_texto} - "hotkey: ", "ctrl + v"\n'
            logs(text_log)
            archive.close()
                
    except Exception:
        print(Exception)

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

        filename_location = filename.split("/")
        filename_location = filename_location[-1]
        data_e_hora_atuais = datetime.now()
        hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S')
        text_log = f'{hora_em_texto} - "executed: ", {filename_location}"\n'
        logs(text_log)

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
            print("Erro aqui: final")
            print(Exception)
    else:
        print("No file selected.")

button_mode = True
def customize():

    global button_mode
    if button_mode:
        button_toogle.configure(image=button_image_off, fg_color='transparent')
        customtkinter.set_appearance_mode("dark")
        app.config(bg="black", bd=0)
        button_mode = False

    else:
        button_toogle.configure(image=button_image_on, fg_color='transparent')
        customtkinter.set_appearance_mode("light")
        button_mode = True

button_visible = True
def see():

    global button_visible
    if button_visible:
        button_see.configure(image=button_see_off)
        app.call('wm', 'attributes', '.', '-topmost', True)
        app.after_idle(app.call, 'wm', 'attributes', '.', '-topmost', True)
        button_visible = False

    else:
        button_see.configure(image=button_see_on)
        # the window will stay in the principal layer(in front)
        app.call('wm', 'attributes', '.', '-topmost', False)
        app.after_idle(app.call, 'wm', 'attributes', '.', '-topmost', False)
        button_visible = True

########################################################## FRAMES #################################################################################

#frame that will contain the buttons
frame_buttons = customtkinter.CTkFrame(master=app, width=250, height=400)
frame_buttons.pack(side="left", padx=20, pady=40)

#frame that will contain the inputs and configs
frame_config = customtkinter.CTkFrame(master=app, width=400, height=400)
frame_config.pack(side="top", padx=20, pady=10)

########################################################## IMAGES #################################################################################

button_image_on = customtkinter.CTkImage(Image.open("img/light.png"), size=(55,27))
button_image_off = customtkinter.CTkImage(Image.open("img/dark.png"), size=(55,27))
button_see_on = customtkinter.CTkImage(Image.open("img/button-on.png"), size=(45,18))
button_see_off = customtkinter.CTkImage(Image.open("img/button-off.png"), size=(45,18))

########################################################## GUI ####################################################################################

#frame that will contain the title
#automata_name_frame = customtkinter.CTkFrame(frame_buttons, fg_color='transparent')
#automata_name_frame.pack(pady=2)
title_name_app = customtkinter.CTkLabel(master=app, fg_color='transparent', text="AUTOMATA", font=font_tuple).place(x=120, y=5)
#title_name_app.pack(pady=2, padx=1, side='right', anchor='n', expand=True)


#frame that will contain the button create and entry
entry_create_frame = customtkinter.CTkFrame(frame_buttons, fg_color='transparent')
entry_create_frame.pack(pady=5)
entry_name_file = customtkinter.CTkEntry(master=entry_create_frame, border_color="black", placeholder_text="File name?", width=170, font=font_text)
button_create = customtkinter.CTkButton(master=entry_create_frame, border_color="black",  width=120, text="Create file", command=create_archive)
button_create.pack(pady=2, padx=3, side='right', anchor='n', expand=True)
entry_name_file.pack(pady=2, padx=3, side='left', anchor='n', expand=True)


#frame that will contain the button choose
choose_frame = customtkinter.CTkFrame(frame_buttons, fg_color='transparent')
choose_frame.pack(pady=5)
button_choose = customtkinter.CTkButton(master=choose_frame, width=140, text="Select file", command = choose_archive)
button_choose.pack(pady=2, padx=2, side='left', anchor='s', expand=True)


#frame that will contain the button delete
delete_frame = customtkinter.CTkFrame(frame_buttons, fg_color='transparent')
delete_frame.pack(pady=5)
button_delete = customtkinter.CTkButton(master=delete_frame, width=140, text="Delete File", command=delete_archive)
button_delete.pack(pady=2, padx=2, side='left', anchor='n', expand=True)


#frame that will contain the button save mouse(left)
save_mouse_left_frame = customtkinter.CTkFrame(frame_buttons, fg_color='transparent')
save_mouse_left_frame.pack(pady=5)
button_get_mouse_left = customtkinter.CTkButton(master=save_mouse_left_frame, width=140, text="Save mouse(left)", command=get_mouse_left)
button_get_mouse_left.pack(pady=2, padx=2, side='left', anchor='s', expand=True)


#frame that will contain the button save mouse(right)
save_mouse_right_frame = customtkinter.CTkFrame(frame_buttons, fg_color='transparent')
save_mouse_right_frame.pack(pady=5)
button_get_mouse_right = customtkinter.CTkButton(master=save_mouse_right_frame, width=140, text="Save mouse(right)", command=get_mouse_right)
button_get_mouse_right.pack(pady=2, padx=2, side='left', anchor='s', expand=True)


#frame that will contain the button entry and keyboard
entry_execute_frame = customtkinter.CTkFrame(frame_buttons, fg_color='transparent')
entry_execute_frame.pack(pady=5)
textbox = customtkinter.CTkEntry(master=entry_execute_frame, placeholder_text="Write something here...", width=170, border_color="black",font=font_text)
button_keyboard = customtkinter.CTkButton(master=entry_execute_frame, border_color="black", width=120, text="Save keyboard", command=receive_text)
button_keyboard.pack(pady=2, padx=3, side='right', anchor='n', expand=True)
textbox.pack(pady=2, padx=3, side='left', anchor='n', expand=True)


#frame that will contain the button create and execute
execute_frame = customtkinter.CTkFrame(frame_buttons, fg_color='transparent')
execute_frame.pack(pady=5)
button_execute = customtkinter.CTkButton(master=execute_frame, bg_color='transparent',  border_color="black", width=120, text="Execute file", command=autobot, fg_color="lightgreen", hover_color="green", text_color="black")
button_execute.pack(pady=2, padx=60, side='left', anchor='e', expand=True)


#button that change the theme(dark/light)
toogle_theme_frame_and_see = customtkinter.CTkFrame(frame_buttons, fg_color='transparent')
toogle_theme_frame_and_see.pack(pady=5)
button_toogle = customtkinter.CTkButton(master=toogle_theme_frame_and_see, fg_color='transparent', bg_color='transparent', border_width=0, hover='transparent', image=button_image_on, text='', command=customize)
button_toogle.pack(pady=2, padx=10, side='left', anchor='w')
#button see and unsee(visible or not)
button_see = customtkinter.CTkButton(master=toogle_theme_frame_and_see, height=10, fg_color='transparent', bg_color='transparent', border_width=0, hover='transparent', image=button_see_on, text='', command=see)
button_see.pack(pady=2, padx=10, side='right', anchor='e')


#slider and button that save the input
slider_clicks_frame = customtkinter.CTkFrame(frame_config, fg_color='transparent')
slider_clicks_frame.pack(pady=2)
slider_clicks = customtkinter.CTkSlider(master=slider_clicks_frame, number_of_steps=2, from_=1, to=3)
button_slider_clicks = customtkinter.CTkButton(master=slider_clicks_frame, width=100, text="Save clicks", command=slider_click)
slider_clicks.set(1)
button_slider_clicks.pack(pady=2, padx=3, side='right', anchor='e', expand=True)
slider_clicks.pack(pady=6, padx=3)


#slider vel and button that save the input
vel_slider_frame = customtkinter.CTkFrame(frame_config, fg_color='transparent')
vel_slider_frame.pack(pady=2)
slider_velocity= customtkinter.CTkSlider(master=vel_slider_frame, number_of_steps=200, from_=0.05, to=10)
button_slider_vel = customtkinter.CTkButton(master=vel_slider_frame, width=100,  text=" Save Vel.", command=slider_vel)
slider_velocity.set(0.05)
button_slider_vel.pack(pady=2, padx=3, side='right', anchor='e', expand=True)
slider_velocity.pack(pady=6, padx=3)


#buttons hotkeys
hotkeys_frame = customtkinter.CTkFrame(frame_config, fg_color='transparent')
hotkeys_frame.pack(pady=2)
hotkey_select_all = customtkinter.CTkButton(master=hotkeys_frame, width=60, text="ctrl + a", command=funct_select_all)
hotkey_copy = customtkinter.CTkButton(master=hotkeys_frame, width=60, text="ctrl + c", command=funct_copy)
hotkey_paste = customtkinter.CTkButton(master=hotkeys_frame, width=60, text="ctrl + v", command=funct_paste)
hotkey_select_all.pack(pady=4, padx=5, side="left")
hotkey_copy.pack(pady=4, padx=5, side="left")
hotkey_paste.pack(pady=4, padx=5, side="left")


#frame user logs
log_text_frame = customtkinter.CTkFrame(frame_config, fg_color='transparent')
log_text_frame.pack(pady=2)
log_text = customtkinter.CTkLabel(master=log_text_frame, text="log")
log_text.pack()
log_frame = customtkinter.CTkFrame(frame_config, fg_color='transparent')
log_frame.pack(pady=4)
log_label = customtkinter.CTkTextbox(master=log_frame, border_color="black", width=250, height=250, font=font_text)
log_label.insert("0.0", text_log)
log_label.pack(pady=5)



app.mainloop()