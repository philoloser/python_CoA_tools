import os
import shutil
import psutil

print("\n")
print(
    "--------------------------------------------------------------------------------"
)
print(
    "                           ¤ CERTYFIKATY NAZYWARKA ¤                            "
)
print(
    "--------------------------------------------------------------------------------"
)
print("\n")

sciezka_source = "C:\\Users\\i.janowska\\Documents\\OUTLOOKZALACZNIKI"
sciezka_dest = (
    "C:\\Users\\i.janowska\\Torf Corporation Sp. z o.o\\"
    "KJ - _Sharepoint_TC\\QC kontrola jakosci\\surowce"
    "\\Certyfikaty\\Certyfikaty\\CERTYFIKATY 2024"
)

cont = 1
while cont == 1:

    # nadawanie nazwy + otwieranie cdn'u
    while cont == 1:

        print("¤ GK czy B?")
        print("1. GK")
        print("2. B")
        gk_b = input()

        if gk_b == "1":  # nasze gk
            print(
                "--------------------------------------------------------------------------------"
            )
            gk_cert = input("¤ Wprowadź GK i CDN: ").upper()
            cdn = gk_cert[-6:]
            if gk_cert.__contains__("/"):
                nrgk = gk_cert.split("/")[0]
                gk_cert = nrgk + ". " + cdn
                print(">>> Wybrany certyfikat: " + gk_cert)
                print(
                    "--------------------------------------------------------------------------------"
                )
            else:
                print(">>> Wybrany certyfikat: " + gk_cert)
                print(
                    "--------------------------------------------------------------------------------"
                )

            path = (
                "C:\\Users\\i.janowska\\OneDrive - Torf Corporation Sp. z o.o\\"
                "Zalaczniki do CHECK LISTY" + "\\" + cdn
            )
            path = os.path.realpath(path)
            if os.path.exists(path):
                os.startfile(path)
            else:
                print("Folder CDN nie istnieje.")
                print(
                    "--------------------------------------------------------------------------------"
                )
            break
        if gk_b == "2":  # bielenda
            print(
                "--------------------------------------------------------------------------------"
            )
            print("¤ Wprowadź datę i CDN:")
            b_cert = input().upper()
            if b_cert.__contains__("B"):
                bnr = b_cert.split(".")[0]
                bnr2 = b_cert.split(".")[1]
                cdn = b_cert.split(".")[2][-6:]
                b_cert = bnr + "." + bnr2 + " " + cdn
                print(">>> Wybrany certyfikat: " + b_cert)
                print(
                    "--------------------------------------------------------------------------------"
                )
            else:
                print(">>> Wybrany certyfikat: " + b_cert)
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
            )  # RETURN TO WHILE
            print(
                "--------------------------------------------------------------------------------"
            )

            continue

    # otwieranie pdf'a
    while cont == 1:

        print("¤ Szukanie PDF'a:")
        print("1. AUTOMAT")
        print("2. RĘCZNIE")
        szukanie = input()

        if szukanie == "1":
            while szukanie == "1":
                print("Szukanie pliku...")

                sciezka_source = os.path.abspath(sciezka_source)
                # Set to hold opened PDF files (using a set for faster lookups)
                open_pdf_files = set()

                # Loop through all running processes
                for proc in psutil.process_iter(['pid', 'name', 'open_files']):
                    try:
                        # Get the list of open files for the process
                        open_files = proc.info['open_files']
                        if open_files:  # Check if there are any open files
                            # Use a list comprehension to filter and add opened PDF files
                            open_pdf_files.update(
                                file.path for file in open_files
                                if file.path.lower().endswith('.pdf') and os.path.dirname(file.path).lower() == sciezka_source.lower()
                            )
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue

                # Print the results
                if open_pdf_files:
                    print(">>> Otwarty plik:")
                    for f in open_pdf_files:
                        f = f.split('\\')[-1]
                        print(f)
                        print(
                            "--------------------------------------------------------------------------------"
                        )
                    break

                else:
                    print("Brak otwartego pliku.")
                    continue
            break

        if szukanie == "2":
            f = input("¤ Wprowadź nazwę PDF: ")
            f = f + '.pdf'
            print(">>> Wybrany plik: " + f)
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
            )
            print(
                "--------------------------------------------------------------------------------"
            )
            continue

    # zapisywanie cert
    while cont == 1:
        print("¤ Czy zapisać certyfikat?")
        print("1. OK")
        print("2. NIE")
        poprawne = input()
        if poprawne == "1":
            if gk_b == "1":
                source = sciezka_source + "\\" + f
                dest = sciezka_dest + "\\" + gk_cert + ".pdf"
                shutil.copyfile(source, dest)
            if gk_b == "2":
                source = sciezka_source + "\\" + f
                dest = sciezka_dest + "\\" + b_cert + ".pdf"
                shutil.copyfile(source, dest)
            print(
                "--------------------------------------------------------------------------------"
            )
            print(
                "                ¤ SUKCES. CERTYFIKATY NAZYWARKA jedzie dalej! ¤                 "
            )
            print(
                "--------------------------------------------------------------------------------"
            )
            break

        if poprawne == "2":
            print(
                "--------------------------------------------------------------------------------"
            )
            print(
                "                   ¤ KLAPA! CERTYFIKAT nie został zapisany! ¤                    "
            )
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
            )  # RETURN TO WHILE
            print(
                "--------------------------------------------------------------------------------"
            )
            continue
