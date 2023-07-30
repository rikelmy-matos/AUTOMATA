from tkinter import filedialog

#function that choose and save an archive path
def choose_archive():

    filename = filedialog.askopenfilename()
    if filename !='':
        with open("controlpy/choose.txt", 'w') as archive:
            archive.write(filename)
    else:
        print("No file selected.")
