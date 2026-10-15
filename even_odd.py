# Kontrolli, kas sisestatud täisarv on paaris või paaritu
n = int(input("Sisesta täisarv: "))

match n % 2:
    case 0:
        print("Arv on paaris")
    case _:
        print("Arv on paaritu")