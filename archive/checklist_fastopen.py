import os
import glob

petlowanie = 1

while petlowanie == 1:
    cdn = input("Wpisz KOD: ")
    path = (
        r"C:\Users\i.janowska\OneDrive - Torf Corporation Sp. z o.o\Zalaczniki do CHECK LISTY"
    )

    path = path + '\\' + cdn + '*'
    path = glob.glob(path)
    print(path)

    path = ''.join(path)

    path = os.path.realpath(path)
    if os.path.exists(path):
        os.startfile(path)
    else:
        print("Folder CDN nie istnieje.")
        print(
            "--------------------------------------------------------------------------------"
        )