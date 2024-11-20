import os
import glob

petlowanie = 1 # Purely to loop the block of code

while petlowanie == 1:
    cdn = input("¤ Wpisz GK/CDN: ").upper()
    path = (
        "C:\\Users\\i.janowska\\Torf Corporation Sp. z o.o\\"
        "KJ - _Sharepoint_TC\\QC kontrola jakosci\\surowce"
        "\\Certyfikaty\\Certyfikaty\\CERTYFIKATY 2024\\"
    )

    path = path + '*' + cdn + '*' # Combining sourcepath and cdn with wildcards
    path = glob.glob(path) # Searching through sourcepath (creates a list)
    path.sort(reverse=True) # Sort in ascending order

    loopcount = 1 # Initialize a loopcount
    files = {} # Initialize a dictionary

    print('\n')
    print('¤ Wybierz certyfikat:')

    for p in path: # Iterate through the path list

        files[loopcount.__str__()] = p # Dictionary | loopcount: path | Changing loopcount to str; compatible with input
        lp = loopcount.__str__() + '. ' + p.split('\\')[-1].replace('.pdf', '') # 1. 1001. SC0001 | Take the last item after split | Removing .pdf
        print(lp)
        loopcount = loopcount + 1 # Increment the loopcount

    choice = input()
    print(files[choice])

    openfile = os.path.realpath(files[choice])
    if os.path.exists(openfile):
        os.startfile(openfile)
    else:
        print("Folder CDN nie istnieje.")
        print(
            "--------------------------------------------------------------------------------"
        )
