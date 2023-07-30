import os
from tkinter import filedialog


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

    else:
        print("No file selected.")
