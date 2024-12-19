
import shutil
import os
import glob
from pathlib import Path, PurePath

print("                            ¤ DUPLIKATY NAZYWARKA ¤                             ")
print("--------------------------------------------------------------------------------")

coa_dir_name = r'\certyfikaty_' + '2024'

# This could also be resolved with pathlib PurePath().parents[n] | shorter version, more sensitive to folder changes
# Insensitive to folder changes from 'surowce' | using glob.glob

# Path to script
script_path = r'c:\Users\i.janowska\OneDrive - Torf Corporation Sp. z o.o\_Sharepoint_TC\QC kontrola jakosci\surowce\Certyfikaty\programy\CoA_naming_duplicate_klaudia.exe' # os.path.dirname(os.path.realpath(__file__))
# Path to '\surowce'
script_char = script_path.find('surowce') + len('surowce')
parent_path = script_path[:script_char]
# Path tail to CoA folder
coa_dir_path = r'Certyfikaty' + coa_dir_name
# Path joining for full CoA folder path
coa_dir_path = os.path.realpath(os.path.join(parent_path, coa_dir_path))

cont = "1"

while cont == "1":
    # ----------------------------------------------------------------------- OLD GK/B

    while cont == "1":
        print("¤ Stary certyfikat: GK czy B?")  # OLD GK/B
        print("1. GK")
        print("2. B")
        oldgk_b = input()

        if oldgk_b == "1":  # OLD GK
            print(
                "--------------------------------------------------------------------------------"
            )
            gk_old = input("¤ Wprowadź stare GK i CDN: ").upper()
            cdn = gk_old[-6:]

            if gk_old.__contains__("/"):  # OLD GK CONTAINS /
                nr_old = gk_old.split("/")[0]
                old = nr_old + ". " + cdn
                print(">>> Wybrany certyfikat: " + old)
                print(
                    "--------------------------------------------------------------------------------"
                )
            else:
                old = gk_old  # OLD GK WITHOUT /
                print(">>> Wybrany certyfikat: " + old)
                print(
                    "--------------------------------------------------------------------------------"
                )
            break
        if oldgk_b == "2":  # OLD B
            print(
                "--------------------------------------------------------------------------------"
            )
            b_old = input("¤ Wprowadź starą datę i CDN: ").upper()  # OLD B CONTAINS "B"
            if b_old.__contains__("B"):
                bnr_old = b_old.split(".")[0]
                bnr_old2 = b_old.split(".")[1]
                old = bnr_old + "." + bnr_old2 + " " + cdn
                print(">>> Wybrany stary certyfikat: " + old)
                print(
                    "--------------------------------------------------------------------------------"
                )
            else:  # OLD B WITHOUT "B"
                old = b_old
                print(">>> Wybrany certyfikat: " + old)
                print(
                    "--------------------------------------------------------------------------------"
                )
            break
        else:
            print(
                "--------------------------------------------------------------------------------"
            )
            print(
                "                          Wpisano niepoprawną wartość.                          "
            )  # RETURN TO WHILE cont
            print(
                "--------------------------------------------------------------------------------"
            )
            continue

    # ----------------------------------------------------------------------- NEW GK/B

    while oldgk_b == "1" or "2":
        print("¤ Nowy certyfikat: GK czy B?")  # NEW GK/B
        print("1. GK")
        print("2. B")
        newgk_b = input()
        if newgk_b == "1":  # NEW GK
            print(
                "--------------------------------------------------------------------------------"
            )
            gk_new = input("¤ Wprowadź nowe GK: ").upper()
            if gk_new.__contains__("/"):  # NEW GK CONTAINS /
                nr_new = gk_new.split("/", 1)[0]
                new = nr_new + ". " + cdn
                print(">>> " + old + " -> " + new)
                print(
                    "--------------------------------------------------------------------------------"
                )
            else:
                new = gk_new + ". " + cdn  # NEW GK WITHOUT /
                print(">>> " + old + " -> " + new)
                print(
                    "--------------------------------------------------------------------------------"
                )
            break
        if newgk_b == "2":  # NEW B
            print(
                "--------------------------------------------------------------------------------"
            )
            b_new = input("¤ Wprowadź nową datę: ").upper()
            count = b_new.count('.')
            if count == 2:
                bnr_new = b_new.split(".")[0]
                bnr_new2 = b_new.split(".")[1]
                new = bnr_new + "." + bnr_new2 + " " + cdn
                print(">>> " + old + " -> " + new)
                print(
                    "--------------------------------------------------------------------------------"
                )
            else:
                new = b_new + " " + cdn
                print(">>> " + old + " -> " + new)
                print(
                    "--------------------------------------------------------------------------------"
                )
            break
        else:
            print(
                "--------------------------------------------------------------------------------"
            )
            print(
                "                          Wpisano niepoprawną wartość.                          "
            )  # RETURN TO WHILE oldgk_b
            print(
                "--------------------------------------------------------------------------------"
            )
            continue

    # ----------------------------------------------------------------------- POPRAWNE

    print("¤ Czy dane są poprawne?")
    print("1. OK")
    print("2. NIE")
    poprawne = input()

    if poprawne == "1":
        source = coa_dir_path + "\\" + old + ".pdf"
        dest = coa_dir_path + "\\" + new + ".pdf"
        shutil.copy(source, dest)
        print(
            "--------------------------------------------------------------------------------"
        )
        print(
            "                ¤ SUKCES! DUPLIKATY NAZYWARKA jedzie dalej! ¤                   "
        )
        print(
            "--------------------------------------------------------------------------------"
        )
    else:
        print
        print(
            "--------------------------------------------------------------------------------"
        )
        print(
            "                   ¤ KLAPA! DUPLIKAT nie został utworzony! ¤                    "
        )
        print(
            "--------------------------------------------------------------------------------"
        )
        continue
