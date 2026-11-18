import tkinter as tk
from tkinter import messagebox
from pathlib import Path

SLOZKA = Path(__file__).resolve().parent


def nacti_postavy(cesta):
    postavy = []
    chyby = []
    try:
        with open(cesta, encoding="utf-8-sig") as soubor:
            for cislo, radek in enumerate(soubor, 1):
                if not radek.strip():
                    continue
                try:
                    jmeno, vek, pohlavi, zvire, hodnoceni = radek.strip().split(";")
                    jmeno = jmeno.strip()
                    vek = int(vek)
                    pohlavi = pohlavi.strip().lower()
                    zvire = zvire.strip().lower()
                    hodnoceni = float(hodnoceni)
                    if (not jmeno or vek < 0 or pohlavi not in ("muž", "žena")
                            or zvire not in ("ano", "ne") or not 0 <= hodnoceni <= 5):
                        raise ValueError
                    postavy.append({"jmeno": jmeno, "vek": vek,
                                    "pohlavi": pohlavi, "zvire": zvire,
                                    "hodnoceni": hodnoceni})
                except ValueError:
                    chyby.append(f"Řádek {cislo}: neplatný záznam, přeskočeno.")
    except (OSError, UnicodeError) as chyba:
        chyby.append(f"Soubor nelze načíst: {chyba}")
    return postavy, chyby


def uloz_vystup(postavy, cesta):
    # Přípona .py je podle požadavku, obsah je obyčejný text.
    with open(cesta, "w", encoding="utf-8") as soubor:
        for p in postavy:
            if p["pohlavi"] == "muž" and p["hodnoceni"] > 2.5:
                soubor.write(f'{p["jmeno"]};{p["vek"]};{p["pohlavi"]};'
                             f'{p["zvire"]};{p["hodnoceni"]}\n')


def spust():
    postavy, chyby = nacti_postavy(SLOZKA / "postavy.txt")
    index = 0
    okno = tk.Tk()
    okno.title("Filmové postavy")
    okno.resizable(False, False)

    def zobraz():
        if postavy:
            p = postavy[index]
            text.config(text=f'Jméno: {p["jmeno"]}\nVěk: {p["vek"]}\n'
                             f'Pohlaví: {p["pohlavi"]}\nZvíře: {p["zvire"]}\n'
                             f'Hodnocení: {p["hodnoceni"]} / 5')
            poradi.config(text=f"Postava {index + 1} z {len(postavy)}")
        else:
            text.config(text="Žádné platné postavy.")
            poradi.config(text="Postava 0 z 0")
        predchozi.config(state="normal" if index > 0 else "disabled")
        dalsi.config(state="normal" if index < len(postavy) - 1 else "disabled")

    def posun(krok):
        nonlocal index
        if 0 <= index + krok < len(postavy):
            index += krok
        zobraz()

    def uloz():
        try:
            uloz_vystup(postavy, SLOZKA / "vystup.py")
            stav.config(text="Muži s hodnocením > 2,5 uloženi do vystup.py.")
        except (OSError, UnicodeError) as chyba:
            messagebox.showerror("Chyba ukládání", str(chyba), parent=okno)

    text = tk.Label(okno, justify="left", width=38, anchor="w", padx=15, pady=15)
    text.pack()
    poradi = tk.Label(okno)
    poradi.pack()
    tlacitka = tk.Frame(okno)
    tlacitka.pack(pady=10)
    predchozi = tk.Button(tlacitka, text="Předchozí", command=lambda: posun(-1))
    predchozi.pack(side="left", padx=5)
    dalsi = tk.Button(tlacitka, text="Další", command=lambda: posun(1))
    dalsi.pack(side="left", padx=5)
    tk.Button(okno, text="Uložit vybrané muže", command=uloz).pack()
    stav = tk.Label(okno, text="", wraplength=330, padx=10, pady=10)
    stav.pack()
    zobraz()
    if chyby:
        messagebox.showwarning("Chyby při načítání", "\n".join(chyby), parent=okno)
    uloz()
    okno.mainloop()


if __name__ == "__main__":
    spust()
