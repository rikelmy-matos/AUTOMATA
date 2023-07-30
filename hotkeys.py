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
                
    except Exception:
        print(Exception)