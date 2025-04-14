# Python GUI

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa dia")

# frame input
input_frame = ttk.Frame(window)
nama_depan=tk.StringVar()
nama_belakang = tk.StringVar()

def tombol_click():
    '''ini akan dipanggil oleh tombol'''
    pesan = f"Halo {nama_depan.get()} {nama_belakang.get()} asuu jancok!!"
    showinfo(title="whazzuppp!!",message=pesan)

# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. label untuk nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama depan")
nama_depan_label.pack(padx=10,pady=10,fill="x",expand=True)

# 2. nama depan entry
nama_depan_entri = ttk.Entry(input_frame,textvariable=nama_depan)
nama_depan_entri.pack(padx=10, fill="x",expand=True)

# 3. label untuk nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang")
nama_belakang_label.pack(padx=10,pady=10,fill="x",expand=True)

# 4. nama belakang entry
nama_belakang=tk.StringVar()
nama_belakang_entri = ttk.Entry(input_frame,textvariable=nama_belakang)
nama_belakang_entri.pack(padx=10, fill="x",expand=True)

# 5. Tombol
tombol_sapa = ttk.Button(input_frame,text="Sapa!",command = tombol_click)
tombol_sapa.pack(fill="x",expand=True,padx=10,pady=10)

window.mainloop()