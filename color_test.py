from colorama import Fore, Style

# Küsi lemmikvärv ja väljasta selle põhjal temperament
color = input("Sisesta oma lemmikvärv: ").lower()

match color:
    case "punane":
        print(Fore.RED + "Sa oled energiline inimene!" + Style.RESET_ALL)
    case "roosa":
        print(Fore.MAGENTA + "Sa oled romantik!" + Style.RESET_ALL)
    case "roheline":
        print(Fore.GREEN + "Sa oled rahulik inimene!" + Style.RESET_ALL)
    case "sinine":
        print(Fore.BLUE + "Sa oled keskendunud inimene!" + Style.RESET_ALL)
    case _:
        print(Fore.CYAN + "Sa oled imeline ükssarvik!" + Style.RESET_ALL)