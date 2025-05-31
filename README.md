# Igra Zmija

# Sadržaj
1. [O igri općenito](#o-igri-općenito)
2. [Pokretanje igre](#pokretanje-igre)
3. [Korišteni alati](#korišteni-alati)
4. [Kontrole](#kontrole)

# O igri općenito
Igra Zmija je žanr akcionih video igara u kojima igrač upravlja zmiju. <br>
Zadatak igrača u mojoj igri je da spriječi da zmija dođe u kontakt sa vlastitim tijelom,što postaje sve teže kako se zmija izdužuje. <br>
Zmija se izdužuje tako što jede hranu(miša) i kako se zmija izdužuje tako se i povečava rezultat u igri.

# Pokretanje igre
Prvo trebate da klonirate projekat na terminalu
```bash
git clone https://github.com/FareZrextIT/KobraFare.git
```
Drugo trebate da promjenite direktorij 
```bash
cd .\KobraFare\
```
Treće Trebate instalirati Rye macOS/Linux
```bash
curl -sSf https://rye-up.com/get
```
Rye Windows 64-bit (x86-64) i  32-bit (x86)

[rye-x86_64-windows.exe](https://rye.astral.sh/guide/installation/#installing-rye) <br> [rye-x86-windows.exe](https://rye.astral.sh/guide/installation/#installing-rye)


Rye Scoop instaliranje 
```bash
scoop install rye 
```
Četvrto sinkronizujete
```bash
rye sync
```
Peto pokrenete igru
```bash
rye run python .\src\kobrafare\main.py
```


# Korišteni alati

Programski jezik koji je korišten je: Python <br>
Biblioteke: Pygame(za razvoj igre) <br>
Package Manager: Rye <br>
Razvojno okruženje: Visual Studio Code <br>

# Kontrole 
Zmija se kreće tipkama WASD, i ide gore,delo i lijevo,desno.
Na početku će biti ekran na kojem će pisati pritisnite tipku space na tastaturi koja ima funkciju start dugmeta.
Tipkom P igra se pauzira.


# Početni ekran
![image](https://github.com/user-attachments/assets/14832df7-56aa-4d42-aac1-4cdd61c6c9b9)


# Ekran Igre
![Ekran igre](https://github.com/user-attachments/assets/487618ae-f884-482c-862f-aee85815c7cd)




# Pauza ekran
![image](https://github.com/user-attachments/assets/f59d4535-f234-447b-a8ac-7bcf118743ac)


