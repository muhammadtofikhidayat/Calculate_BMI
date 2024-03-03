import tkinter as tk
from tkinter import ttk
import sqlite3
import webbrowser as web
import sqlite3


def open_web():
    url = "http://127.0.0.1:5500/BMI1.html"
    web.open(url)
    

def create_table():
    # Membuat tabel jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pasien (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            tinggi INTEGER,
            berat INTEGER
        )
    ''')
    connection.commit()

def insert_data(name, age, tinggi, berat):
    #priksa data tidak boleh kosong
    if not name or not age or not tinggi or not berat:
        print("data tidak ada yang boleh kosong")
    # Menyisipkan data ke dalam tabel
    else:
        cursor.execute('INSERT INTO pasien (name, age, tinggi, berat) VALUES (?, ?, ?, ?)', (name, age,tinggi, berat))
        connection.commit()
        show_data()
        open_web()

def update_data(selected_item, new_name, new_age, new_tinggi, new_berat):
    try:
        selected_id = tree.item(selected_item)['values'][0]
        with sqlite3.connect("pasien.db") as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE pasien SET name=?, age=? , tinggi=?, berat=? WHERE id=?", (new_name, new_age,new_tinggi,new_berat, selected_id))
            connection.commit()
            show_data()
            print(selected_id)
            print("Data berhasil diupdate.")
    except sqlite3.Error as error:
        print("Error:", error)


def show_data():
    # Mengambil data dari tabel dan menampilkannya di Treeview
    cursor.execute('SELECT * FROM pasien')
    data = cursor.fetchall()
    tree.delete(*tree.get_children())
    for row in data:
        tree.insert('', 'end', values=row)

def delete_last_data(selected_item):
    try:
        # Mendapatkan ID data terakhir dalam tabel
        cursor.execute("SELECT * FROM pasien")
        last_id = tree.item(selected_item)['values'][0]

        # Menghapus data terakhir berdasarkan ID
        cursor.execute("DELETE FROM pasien WHERE id=?", (last_id,))

        # Commit perubahan
        connection.commit()

        # Menampilkan data terbaru setelah penghapusan
        show_data()

        print("Data berhasil dihapus.")

    except sqlite3.Error as error:
        print("Error:", error)


def on_item_select(event):
    selected_item = tree.item(tree.selection())
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    tinggi_entry.delete(0, tk.END)
    berat_entry.delete(0, tk.END)
    name_entry.insert(0, selected_item['values'][1])
    age_entry.insert(0, selected_item['values'][2])
    tinggi_entry.insert(0, selected_item['values'][3])
    berat_entry.insert(0, selected_item['values'][4])

def update_selected_data():
    # Mendapatkan data terpilih dari Treeview
    selected_item = tree.focus()

    # Memastikan ada item yang terpilih
    if selected_item:
        new_name = name_entry.get()
        new_age = age_entry.get()
        new_tinggi = tinggi_entry.get()
        new_berat = berat_entry.get()

        # Memanggil fungsi untuk melakukan update data
        update_data(selected_item, new_name, new_age, new_tinggi, new_berat)
    else:
        print("Pilih item terlebih dahulu untuk melakukan update.")

def delete_selected_data():
    # Mendapatkan data terpilih dari Treeview
    selected_item = tree.focus()

    # Memastikan ada item yang terpilih
    if selected_item:
        new_name = name_entry.get()
        new_age = age_entry.get()
        new_tinggi = tinggi_entry.get()
        new_berat = berat_entry.get()

        # Memanggil fungsi untuk melakukan update data
        delete_last_data(selected_item)
    else:
        print("Pilih data yang akan di delete.")

# Membuat jendela utama
window = tk.Tk()
window.title("BMI CALCULATOR")

# Membuat koneksi ke database SQLite
connection = sqlite3.connect("pasien.db")
cursor = connection.cursor()

# Membuat tabel (jika belum ada)
create_table()

name_label = tk.Label(window, text="Nama:")
name_entry = tk.Entry(window)
age_label = tk.Label(window, text="Usia:")
age_entry = tk.Entry(window)
tinggi_label = tk.Label(window, text="Tinggi:")
tinggi_entry = tk.Entry(window)
berat_label = tk.Label(window, text="Berat:")
berat_entry = tk.Entry(window)
insert_button = tk.Button(window, text="Tambahkan Data", command=lambda: insert_data(name_entry.get(), age_entry.get(), tinggi_entry.get(), berat_entry.get()))
update_button = tk.Button(window, text="Update Data", command=lambda:update_selected_data())
delete_button = tk.Button(window, text="Hapus Data", command=lambda:delete_selected_data())

tree = ttk.Treeview(window, columns=("ID", "Nama", "Usia", "Tinggi", "Berat"), show="headings") 
tree.heading("ID", text="ID")
tree.heading("Nama", text="Nama")
tree.heading("Usia", text="Usia")
tree.heading("Tinggi", text="Tinggi")
tree.heading("Berat", text="Berat")
tree.bind("<ButtonRelease-1>", on_item_select)
show_data()

name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry.grid(row=0, column=1, padx=10, pady=10)
age_label.grid(row=1, column=0, padx=10, pady=10)
age_entry.grid(row=1, column=1, padx=10, pady=10)
tinggi_label.grid(row=2, column=0, padx=10, pady=10)
tinggi_entry.grid(row=2, column=1, padx=10, pady=10)
berat_label.grid(row=3, column=0, padx=10, pady=10)
berat_entry.grid(row=3, column=1, padx=10, pady=10)
insert_button.grid(row=4, column=0, pady=10)
update_button.grid(row=4, column=1, pady=10)
delete_button.grid(row=4, column=2, pady=10)
tree.grid(row=5, column=0, columnspan=3, pady=10, padx=10)

window.mainloop()