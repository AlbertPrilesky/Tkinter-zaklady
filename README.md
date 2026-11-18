# Tkinter-zaklady

Jednoduchá školní aplikace pro listování filmovými postavami.

Spuštění: `py python.py` (Python 3 s Tkinterem).

- `postavy.txt`: jméno;věk;pohlaví;zvíře (ano/ne);hodnocení (0 až 5).
- `python.py`: načte seznam slovníků a zobrazí jednu postavu. Tlačítka Předchozí a Další umožňují listování a na okrajích se vypnou.
- `vystup.py`: textový výstup, nikoli spustitelný Python. Obsahuje všechny muže s hodnocením přísně nad 2,5 včetně zvířat. Vzniká při spuštění i po stisknutí tlačítka Uložit vybrané muže.

Neplatné řádky se přeskočí s upozorněním. Chybějící, prázdný nebo nečitelný vstup aplikaci neshodí. Chyba zápisu se zobrazí v dialogu. Soubory se hledají vedle programu.

Věky a hodnocení postav jsou vymyšlené ukázkové údaje.
