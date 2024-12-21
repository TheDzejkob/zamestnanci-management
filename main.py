import tkinter as tk

def add_item():
    name = name_entry.get()
    number = number_entry.get()
    position = position_entry.get()
    if name and number and position:
        item = f"{name},{number},{position}"
        listbox.insert(tk.END, item)
    else:
        error_label.config(text="Vyplňte prosím všechna potřebná pole.")

def remove_item():
    selected_indices = listbox.curselection()
    if selected_indices:
        for index in selected_indices[::-1]:
            listbox.delete(index)

window = tk.Tk()
window.title("Management zamestnancu")

name_label = tk.Label(window, text="Jméno:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

number_label = tk.Label(window, text="Číslo:")
number_label.pack()
number_entry = tk.Entry(window)
number_entry.pack()

position_label = tk.Label(window, text="Oddělení:")
position_label.pack()
position_entry = tk.Entry(window)
position_entry.pack()

add_button = tk.Button(window, text="Přidat", command=add_item)
add_button.pack()

remove_button = tk.Button(window, text="Odebrat", command=remove_item)
remove_button.pack()

error_label = tk.Label(window, fg="red")
error_label.pack()

listbox = tk.Listbox(window)
listbox.pack()

window.mainloop()