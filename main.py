import customtkinter as ctk
from PIL import Image
from logic import Lingkaran, LingkaranPusatO
from plot import gambarGrafik

class LingkaranUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.title("Visualisasi Lingkaran Irisan Kerucut")
        self.geometry("1000x600")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.kiri = ctk.CTkFrame(self, width=360)
        self.kiri.grid(row=0, column=0, sticky="nsew", padx=16, pady=16)
        self.kiri.grid_columnconfigure(0, weight=1)

        self.headerKiri = ctk.CTkLabel(self.kiri, text="Input & Hasil", font=("Monospace", 18, "bold"))
        self.headerKiri.grid(row=0, column=0, padx=10, pady=(10, 4), sticky="w")

        self.subheaderKiri = ctk.CTkLabel(self.kiri, text="Masukkan koordinat pusat dan radius", font=("Monospace", 12))
        self.subheaderKiri.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="w")

        self.inputs = ctk.CTkFrame(self.kiri)
        self.inputs.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.inputs.grid_columnconfigure((0, 1), weight=1)

        self.text_x = ctk.CTkLabel(self.inputs, text="Pusat X")
        self.text_x.grid(row=0, column=0, padx=6, pady=(8, 4), sticky="w")
        self.input_x = ctk.CTkEntry(self.inputs, placeholder_text="mis. 0.0")
        self.input_x.grid(row=1, column=0, padx=6, pady=(0, 8), sticky="ew")

        self.text_y = ctk.CTkLabel(self.inputs, text="Pusat Y")
        self.text_y.grid(row=0, column=1, padx=6, pady=(8, 4), sticky="w")
        self.input_y = ctk.CTkEntry(self.inputs, placeholder_text="mis. 0.0")
        self.input_y.grid(row=1, column=1, padx=6, pady=(0, 8), sticky="ew")

        self.text_r = ctk.CTkLabel(self.inputs, text="Radius r")
        self.text_r.grid(row=2, column=0, padx=6, pady=(4, 4), sticky="w")
        self.input_r = ctk.CTkEntry(self.inputs, placeholder_text="mis. 5.0")
        self.input_r.grid(row=3, column=0, padx=6, pady=(0, 8), sticky="ew")

        self.GunakanPusatO = ctk.CTkCheckBox(self.inputs, text="Pusat di O (0,0)", command=self.pakeLingkaranO)
        self.GunakanPusatO.grid(row=2, column=1, padx=6, pady=(4, 4), sticky="w")

        self.tombol_hitung = ctk.CTkButton(self.inputs, text="Hitung & Gambar", command=self.hitung_dan_gambar)
        self.tombol_hitung.grid(row=3, column=1, padx=6, pady=(0, 8), sticky="ew")

        self.hasil_label = ctk.CTkLabel(self.kiri, text="Hasil")
        self.hasil_label.grid(row=3, column=0, padx=10, pady=(6, 4), sticky="w")

        self.text_hasil = ctk.CTkTextbox(self.kiri, height=240)
        self.text_hasil.grid(row=4, column=0, padx=10, pady=(0, 10), sticky="nsew")
        self.text_hasil.configure(state="disabled")

        self.kanan = ctk.CTkFrame(self)
        self.kanan.grid(row=0, column=1, sticky="nsew", padx=(0, 16), pady=16)
        self.kanan.grid_rowconfigure(0, weight=1)
        self.kanan.grid_columnconfigure(0, weight=1)

        self.image_label = ctk.CTkLabel(self.kanan, text="Grafik akan muncul di sini")
        self.image_label.grid(row=0, column=0, sticky="nsew")

    def pakeLingkaranO(self):
        if self.GunakanPusatO.get():
            self.input_x.delete(0, "end")
            self.input_y.delete(0, "end")
            self.input_x.insert(0, "0")
            self.input_y.insert(0, "0")
            self.input_x.configure(state="disabled")
            self.input_y.configure(state="disabled")
        else:
            self.input_x.configure(state="normal")
            self.input_y.configure(state="normal")

    def tampilkan_pesan(self, pesan: str):
        """Helper untuk menulis pesan ke textbox hasil."""
        self.text_hasil.configure(state="normal")
        self.text_hasil.delete("1.0", "end")
        self.text_hasil.insert("end", pesan.strip() + "\n")
        self.text_hasil.configure(state="disabled")

    def hitung_dan_gambar(self):
        try:
            pusatx = float(self.input_x.get())
            pusaty = float(self.input_y.get())
            r = float(self.input_r.get())
        except ValueError:
            self.tampilkan_pesan("te tot!!! \nInput tidak valid! \nMasukkan angka untuk X, Y, dan Radius.")
            return

        if r <= 0:
            self.tampilkan_pesan("te tot!!! \nRadius tidak valid!\n Radius harus lebih besar dari 0.")
            return

        if self.GunakanPusatO.get():
            lingkaran = LingkaranPusatO(r)
        else:
            lingkaran = Lingkaran(pusatx, pusaty, r)

        hasil = lingkaran.returnHasil()
        self.tampilkan_pesan(hasil)

        gambarGrafik(pusatx, pusaty, r)

        img = ctk.CTkImage(Image.open("hasil.png"), size=(600, 400))
        self.image_label.configure(image=img, text="")
        self.image_label.image = img 


if __name__ == "__main__":
    app = LingkaranUI()
    app.mainloop()

