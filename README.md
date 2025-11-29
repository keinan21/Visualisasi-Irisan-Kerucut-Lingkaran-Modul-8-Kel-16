
# README.md

# Visualisasi Lingkaran (CTk + Matplotlib)

Aplikasi Python untuk menghitung dan memvisualisasikan lingkaran (bagian dari irisan kerucut) dengan antarmuka CustomTkinter dan grafik yang disimpan sebagai PNG menggunakan Matplotlib. Arsitektur modular: perhitungan di `logic.py`, plotting di `plot.py`, dan UI di `ui_ctk.py`.

## Fitur
- Layout bento: panel kiri untuk input (pusat X, pusat Y, radius) dan hasil (textbox); panel kanan untuk gambar lingkaran.
- Tema dark, resolusi tetap 1000x600.
- Validasi sederhana di UI: input numerik (try/except) dan radius harus > 0.
- Gambar disimpan otomatis sebagai `hasil.png` dan ditampilkan dengan `CTkImage`.

## Struktur Proyek
project/
├─ ui_ctk.py        # GUI utama
├─ logic.py         # Kelas Lingkaran & LingkaranPusatO
├─ plot.py          # Fungsi gambarGrafik(x, y, radius, filename="hasil.png")
└─ README.md

## Prasyarat
- Python 3.8+
- Paket: customtkinter, matplotlib, Pillow (PIL)
- Linux/WSL: pastikan Tk tersedia (mis. `python3-tk`)

## Instalasi
# Windows / macOS / Linux
pip install customtkinter matplotlib Pillow

# Catatan: jika ada beberapa versi Python
python -m pip install customtkinter matplotlib Pillow

## Menjalankan
python ui_ctk.py

## Penggunaan Singkat
1. Isi Pusat X, Pusat Y, dan Radius r (atau centang “Pusat di O (0,0)”).
2. Klik “Hitung & Gambar”.
3. Hasil perhitungan muncul di textbox kiri, grafik muncul di kanan dan tersimpan sebagai `hasil.png`.

## Cuplikan Kode Inti

# logic.py (ringkas)
import numpy as np

class Lingkaran:
    def __init__(self, pusatx, pusaty, radius):
        self.radius = radius
        self.pusatx = pusatx
        self.pusaty = pusaty
    def Luas(self): return np.pi * (self.radius ** 2)
    def Keliling(self): return 2 * np.pi * self.radius
    def A(self): return -2 * self.pusatx
    def B(self): return -2 * self.pusaty
    def C(self): return self.pusatx**2 + self.pusaty**2 - self.radius**2
    def returnHasil(self):
        return f"""
Pusat                 : ({self.pusatx}, {self.pusaty})
Radius                : {self.radius}
Luas                  : {self.Luas()}
Keliling              : {self.Keliling()}
Rumus bentuk pertama  : (x - {self.pusatx})² + (y - {self.pusaty})² = {self.radius ** 2}
Rumus bentuk kedua    : x² + y² - {self.A()}x - {self.B()}y + {self.C()} = 0
        """

class LingkaranPusatO(Lingkaran):
    def __init__(self, radius):
        super().__init__(0, 0, radius)
    def returnHasil(self):
        return f"""
Pusat                 : (0, 0)
Radius                : {self.radius}
Luas                  : {self.Luas()}
Keliling              : {self.Keliling()}
Rumus bentuk pertama  : x² + y² = {self.radius ** 2}
Rumus bentuk kedua    : x² + y² - {self.radius ** 2} = 0
        """

# plot.py (ringkas)
import matplotlib.pyplot as plt

def gambarGrafik(x, y, radius, filename="hasil.png"):
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.grid(True)
    circle = plt.Circle((x, y), radius, color='red', fill=False, linewidth=2, zorder=10)
    ax.add_artist(circle)
    ax.set_xlim(x - radius - 1, x + radius + 1)
    ax.set_ylim(y - radius - 1, y + radius + 1)
    ax.set_aspect('equal', adjustable='box')
    ax.set_title('Grafik Lingkaran')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    fig.savefig(filename, dpi=150)
    plt.close(fig)

# ui_ctk.py (ringkas)
import customtkinter as ctk
from PIL import Image
from logic import Lingkaran, LingkaranPusatO
from plot import gambarGrafik

class LingkaranUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark"); ctk.set_default_color_theme("blue")
        self.title("Visualisasi Lingkaran Irisan Kerucut"); self.geometry("1000x600"); self.resizable(False, False)
        self.grid_columnconfigure(0, weight=0); self.grid_columnconfigure(1, weight=1); self.grid_rowconfigure(0, weight=1)

        self.kiri = ctk.CTkFrame(self, width=360); self.kiri.grid(row=0, column=0, sticky="nsew", padx=16, pady=16); self.kiri.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(self.kiri, text="Input & Hasil", font=("Monospace", 18, "bold")).grid(row=0, column=0, padx=10, pady=(10,4), sticky="w")
        ctk.CTkLabel(self.kiri, text="Masukkan koordinat pusat dan radius", font=("Monospace", 12)).grid(row=1, column=0, padx=10, pady=(0,10), sticky="w")
        self.inputs = ctk.CTkFrame(self.kiri); self.inputs.grid(row=2, column=0, padx=10, pady=10, sticky="nsew"); self.inputs.grid_columnconfigure((0,1), weight=1)
        ctk.CTkLabel(self.inputs, text="Pusat X").grid(row=0, column=0, padx=6, pady=(8,4), sticky="w"); self.input_x = ctk.CTkEntry(self.inputs, placeholder_text="mis. 0.0"); self.input_x.grid(row=1, column=0, padx=6, pady=(0,8), sticky="ew")
        ctk.CTkLabel(self.inputs, text="Pusat Y").grid(row=0, column=1, padx=6, pady=(8,4), sticky="w"); self.input_y = ctk.CTkEntry(self.inputs, placeholder_text="mis. 0.0"); self.input_y.grid(row=1, column=1, padx=6, pady=(0,8), sticky="ew")
        ctk.CTkLabel(self.inputs, text="Radius r").grid(row=2, column=0, padx=6, pady=(4,4), sticky="w"); self.input_r = ctk.CTkEntry(self.inputs, placeholder_text="mis. 5.0"); self.input_r.grid(row=3, column=0, padx=6, pady=(0,8), sticky="ew")
        self.GunakanPusatO = ctk.CTkCheckBox(self.inputs, text="Pusat di O (0,0)", command=self.pakeLingkaranO); self.GunakanPusatO.grid(row=2, column=1, padx=6, pady=(4,4), sticky="w")
        ctk.CTkButton(self.inputs, text="Hitung & Gambar", command=self.hitung_dan_gambar).grid(row=3, column=1, padx=6, pady=(0,8), sticky="ew")
        ctk.CTkLabel(self.kiri, text="Hasil").grid(row=3, column=0, padx=10, pady=(6,4), sticky="w")
        self.text_hasil = ctk.CTkTextbox(self.kiri, height=240); self.text_hasil.grid(row=4, column=0, padx=10, pady=(0,10), sticky="nsew"); self.text_hasil.configure(state="disabled")

        self.kanan = ctk.CTkFrame(self); self.kanan.grid(row=0, column=1, sticky="nsew", padx=(0,16), pady=16); self.kanan.grid_rowconfigure(0, weight=1); self.kanan.grid_columnconfigure(0, weight=1)
        self.image_label = ctk.CTkLabel(self.kanan, text="Grafik akan muncul di sini"); self.image_label.grid(row=0, column=0, sticky="nsew")

    def pakeLingkaranO(self):
        if self.GunakanPusatO.get():
            self.input_x.delete(0, "end"); self.input_y.delete(0, "end")
            self.input_x.insert(0, "0"); self.input_y.insert(0, "0")
            self.input_x.configure(state="disabled"); self.input_y.configure(state="disabled")
        else:
            self.input_x.configure(state="normal"); self.input_y.configure(state="normal")

    def tampilkan_pesan(self, pesan: str):
        self.text_hasil.configure(state="normal"); self.text_hasil.delete("1.0", "end"); self.text_hasil.insert("end", pesan.strip() + "\n"); self.text_hasil.configure(state="disabled")

    def hitung_dan_gambar(self):
        try:
            pusatx = float(self.input_x.get()); pusaty = float(self.input_y.get()); r = float(self.input_r.get())
        except ValueError:
            self.tampilkan_pesan("❌ Input tidak valid! Masukkan angka untuk X, Y, dan Radius."); return
        if r <= 0:
            self.tampilkan_pesan("❌ Radius tidak valid! Radius harus lebih besar dari 0."); return

        lingkaran = LingkaranPusatO(r) if self.GunakanPusatO.get() else Lingkaran(pusatx, pusaty, r)
        self.tampilkan_pesan(lingkaran.returnHasil())

        filename = "hasil.png"; gambarGrafik(pusatx, pusaty, r, filename=filename)
        img = ctk.CTkImage(Image.open(filename), size=(600, 400))
        self.image_label.configure(image=img, text=""); self.image_label.image = img

if __name__ == "__main__":
    app = LingkaranUI(); app.mainloop()

## Troubleshooting
- Pastikan `hasil.png` terbentuk dan dapat dibaca oleh Pillow.
- Di Linux/WSL, jika GUI tidak tampil: install paket sistem Tk (`sudo apt install python3-tk`).
- Jika font Monospace tidak ada, gunakan Arial/Inter.

## Kustomisasi Cepat
- Ubah tema: `ctk.set_appearance_mode("light")`.
- Ubah warna garis lingkaran di `plot.py` (parameter `color='red'`).
- Ubah ukuran gambar kanan: `CTkImage(..., size=(lebar, tinggi))`.

## Lisensi
