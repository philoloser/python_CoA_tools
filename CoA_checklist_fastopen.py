import os
import glob
import re

petlowanie = 1

print(
    "--------------------------------------------------------------------------------"
)
print(
    "                     ¤ SZYBKIE OTWIERANIE COA/CHECKLIST ¤                       "
)
print(
    "--------------------------------------------------------------------------------"
)

while petlowanie == 1:

    print('\n')

    petlowanie = 1 # Purely to loop the block of code

    coapath = (
        "C:\\Users\\i.janowska\\Torf Corporation Sp. z o.o\\"
        "KJ - _Sharepoint_TC\\QC kontrola jakosci\\surowce"
        "\\Certyfikaty\\Certyfikaty\\CERTYFIKATY 2024\\"
    )
    checkpath = (
            r"C:\Users\i.janowska\OneDrive - Torf Corporation Sp. z o.o\Zalaczniki do CHECK LISTY" + '\\'
    )

    cdn = input("¤ Wpisz GK/CDN: ").upper()

    coapath = coapath + '*' + cdn + '*' # Combining sourcepath and cdn with wildcards
    coapath = glob.glob(coapath) # Searching through sourcepath (creates a list)
    coapath.sort(reverse=True) # Sort in ascending order

    loopcount = 1 # Initialize a loopcount
    files = {} # Initialize a dictionary

    print('\n')
    print('¤ Wybierz certyfikat:')

    for p in coapath: # Iterate through the path list

        files[loopcount.__str__()] = p # Dictionary | loopcount: path | Changing loopcount to str; compatible with input
        lp = loopcount.__str__() + '. ' + p.split('\\')[-1].replace('.pdf', '') # 1. 1001. SC0001 | Take the last item after split | Removing .pdf
        print(lp)
        loopcount = loopcount + 1 # Increment the loopcount

    if bool(files):
        choice = input()
        if not choice == "":
            openfile = os.path.realpath(files[choice]) # Change to realpath object
            if os.path.exists(openfile): # Check if file exists
                os.startfile(openfile) # Open the file
        else:
            print("Pominięto.")
    else:
        print("Brak CoA.")

    if re.search('[A-Z]', cdn):  # Check if the string contains any letters
        # any(c.isalpha() for c in string_1)
        checkpath = checkpath + cdn
        if os.path.exists(checkpath):  # Check if dir exists
            os.startfile(checkpath)
        else:
            print("Folder CDN nie istnieje.")
    print('\n')
    print(
        "--------------------------------------------------------------------------------"
    )
    continue

