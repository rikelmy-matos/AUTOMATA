import mouse as ms
import customtkinter
from PIL import Image
from choose import choose_archive
from delete import delete_archive
from execute import autobot
from hotkeys import funct_select_all, funct_copy, funct_paste


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

#theme and see variable control
button_mode = True
button_visible = True
#font
font_tuple = ("Roboto", 20, "bold")
font_text = ("Roboto", 13, "normal")


########################################################## FUNCTIONS ##################################################################################
#function that create an archive
def create_archive():

    try:
        archive_name = entry_name_file.get()
        if archive_name != "":
            FileName = str("autopy/" + archive_name + ".txt")
            with open(FileName,"w") as archive:
                archive.close()
            
        else:
            print("Write the name!")
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
                    archive.close()
                
            except Exception:
                print(Exception)
        else:
            print("Write something...")
    except Exception:
                print(Exception)

#function that change the theme
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

#function see and unsee(stay open or not)
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


#function that saves the clicks
def slider_click():
    current_value = int(slider_clicks.get())
    try:
        with open("controlpy/clicks.txt", 'w') as archive:
            archive.write(f'{str(current_value)}|{None}')
    except Exception:
        print(Exception)

#function that saves the clicks
def slider_vel():
    current_value = float(slider_velocity.get())
    current_value = f'{current_value:.2f}'
    try:
        with open("controlpy/vel.txt", 'w') as archive:
            archive.write(f'{current_value}|{None}')

    except Exception:
        print(Exception)

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
slider_velocity= customtkinter.CTkSlider(master=vel_slider_frame, number_of_steps=50, from_=0.2, to=10)
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

#Update new functions
update_frame = customtkinter.CTkFrame(frame_config, fg_color='transparent')
update_frame.pack(pady=2)
update_text = customtkinter.CTkLabel(master=update_frame, text="update soon...")
update_text.pack(pady=4, padx=5)



app.mainloop()