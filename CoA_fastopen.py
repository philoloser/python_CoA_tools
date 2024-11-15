import os
import glob

petlowanie = 1

while petlowanie == 1:
    cdn = input("Wpisz GK: ")
    path = (
        "C:\\Users\\i.janowska\\Torf Corporation Sp. z o.o\\"
        "KJ - _Sharepoint_TC\\QC kontrola jakosci\\surowce"
        "\\Certyfikaty\\Certyfikaty\\CERTYFIKATY 2024\\"
    )

    path = path + cdn + '*'
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
