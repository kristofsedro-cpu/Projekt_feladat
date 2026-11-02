# Reakcióidő-mérő

## Hallgató

Sedró Kristóf

## Feladat leírása

A program a felhasználó reakcióidejét méri. Indítás után a mező pirosra vált, majd véletlen idő múlva zöld lesz, és ekkor kell rákattintani. A program kiírja a mért időt, és a mérésekből statisztikát készít. Ha a felhasználó a zöldre váltás előtt kattint, a kör érvénytelen, és az eredmény nem számít bele a statisztikába.

## Indítás

A programhoz csak a Python beépített moduljai kellenek, külön telepítés nem szükséges.

```bash
python main.py
```

## Modulok és használt függvények

| Modul | Szerepe | Használt függvények |
|---|---|---|
| `random` | Tanult modul, a véletlen várakozási időhöz | `randint()` |
| `statistics` | Bemutatandó modul, a statisztika számításához | `mean()`, `median()`, `stdev()` |
| `time` | Az idő méréséhez | `perf_counter()` |
| `tkinter` | Grafikai modul, az ablakhoz és az eseménykezeléshez | `Tk()`, `Label()`, `title()`, `geometry()`, `pack()`, `config()`, `bind()`, `after()`, `after_cancel()`, `destroy()`, `mainloop()` |
| `tkinter.ttk` | A címke és a gombok megjelenítéséhez | `Label()`, `Button()` |
| `sk_reakcio` | Saját modul | `sk_statisztika()`, `SKReakcioJatek` |

### A bemutatandó modul függvényei

- `statistics.mean()`: a mért idők átlaga
- `statistics.median()`: a sorba rendezett idők középső értéke
- `statistics.stdev()`: a mért idők szórása, vagyis az ingadozásuk mértéke

### Saját függvény

- `sk_statisztika(idok)`: a mért idők listájából elkészíti a kiírandó statisztikát

## Osztály

### `SKReakcioJatek`

Az ablak elemeit és a mérés menetét kezeli.

| Metódus | Feladata |
|---|---|
| `__init__(root)` | Létrehozza az ablak elemeit és beállítja a kezdőértékeket |
| `mezo_beallitas(szoveg, szin)` | Beállítja a mező szövegét és színét |
| `eredmeny_frissites()` | Kiírja a statisztikát |
| `torles()` | Törli a mért időket |
| `kattintas(event)` | Az állapottól függően kezeli a kattintást |
| `inditas()` | Elindítja a véletlen hosszú várakozást |
| `zoldre_valtas()` | Zöldre váltja a mezőt, és elindítja a mérést |
| `tul_korai()` | Leállítja az időzítőt a túl korai kattintásnál |
| `meres_vege()` | Kiszámítja és eltárolja a reakcióidőt |