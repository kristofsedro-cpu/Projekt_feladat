import random
import statistics
import time
import tkinter as tk
from tkinter import ttk

KEK = "#2b6cb0"
PIROS = "#c53030"
ZOLD = "#2f855a"
NARANCS = "#c05621"

def sk_statisztika(idok):
    if not idok:
        return "Még nincs mérés."
    szoras = statistics.stdev(idok) if len(idok) > 1 else 0
    return (
        f"Mérések száma: {len(idok)}\n"
        f"Legjobb idő: {min(idok)} ms\n"
        f"Átlag: {statistics.mean(idok):.0f} ms\n"
        f"Medián: {statistics.median(idok):.0f} ms\n"
        f"Szórás: {szoras:.0f} ms"
    )
    
class SKReakcioJatek:
    def __init__(self, root):
        self.root = root
        self.idok = []
        self.allapot = "kesz"
        self.idozito = None
        self.kezdes = 0
        
        self.root.title("Reakcióidő-mérő")
        self.root.geometry("500x480")
        
        self.mezo = tk.Label(root, font="Arial 18 bold", fg="white", height=8)
        self.mezo.pack(fill="both", expand=True)
        self.mezo.bind("<Button-1>", self.kattintas)
        
        self.eredmeny = ttk.Label(root, font="Arial 12", justify="center")
        self.eredmeny.pack(pady=10)
        
        torles_gomb = ttk.Button(root, text="Eredmények törlése", command=self.torles)
        torles_gomb.pack(pady=(0, 10))
        
        kilepes_gomb = ttk.Button(root, text="Kilépés", command=root.destroy)
        kilepes_gomb.pack(pady=(0, 10))
        
        self.mezo_beallitas("Kattints ide az indításhoz!", KEK)
        self.eredmeny_frissites()
        
    def mezo_beallitas(self, szoveg, szin):
        self.mezo.config(text=szoveg, bg=szin)
        
    def eredmeny_frissites(self):
        self.eredmeny.config(text=sk_statisztika(self.idok))
        
    def torles(self):
        self.idok.clear()
        self.eredmeny_frissites()

    def kattintas(self, event):
        if self.allapot == "kesz":
            self.inditas()
        elif self.allapot == "varakozas":
            self.tul_korai()
        else:
            self.meres_vege()
    
    def inditas(self):
        self.allapot = "varakozas"
        self.mezo_beallitas("Várj, amíg zöld lesz...", PIROS)
        varakozas = random.randint(1500, 4000)
        self.idozito = self.root.after(varakozas, self.zoldre_valtas)
        
    def zoldre_valtas(self):
        self.allapot = "meres"
        self.mezo_beallitas("Kattints most!", ZOLD)
        self.kezdes = time.perf_counter()
        
    def tul_korai(self):
        self.root.after_cancel(self.idozito)
        self.allapot = "kesz"
        self.mezo_beallitas("Túl korán kattintottál!\nKattints az újrakezdéshez.", NARANCS)
        
    def meres_vege(self):
        ido = round((time.perf_counter() - self.kezdes) * 1000)
        self.idok.append(ido)
        self.allapot = "kesz"
        self.mezo_beallitas(f"{ido} ms\nKattints az újrakezdéshez.", KEK)
        self.eredmeny_frissites()
    