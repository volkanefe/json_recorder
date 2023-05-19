import tkinter as tk
import json

def save_record():
    record = {
        "firstName": entry_first_name.get(),
        "lastName": entry_last_name.get(),
        "email": entry_email.get(),
        "phone": entry_phone.get(),
        "city": entry_city.get(),
        "country": entry_country.get(),
        "profession": entry_profession.get()
    }
    data.append(record)
    clear_entries()

def clear_entries():
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_country.delete(0, tk.END)
    entry_profession.delete(0, tk.END)

def save_to_json():
    with open("records.json", "r") as file:
        existing_data = json.load(file)
    existing_data.extend(data)
    with open("records.json", "w") as file:
        json.dump(existing_data, file, indent=4)
    print("Records saved to records.json file.")
    root.destroy()

def show_records():
    records_window = tk.Toplevel(root)
    records_window.title("Records")

    search_label = tk.Label(records_window, text="Search:")
    search_label.pack()

    search_entry = tk.Entry(records_window)
    search_entry.pack()

    listbox_records = tk.Listbox(records_window, width=50)
    listbox_records.pack()

    def search_records():
        query = search_entry.get().lower()
        listbox_records.delete(0, tk.END)
        for record in records:
            full_name = record["firstName"] + " " + record["lastName"]
            if query in full_name.lower():
                listbox_records.insert(tk.END, full_name)

    search_button = tk.Button(records_window, text="Search", command=search_records)
    search_button.pack()

    with open("records.json", "r") as file:
        records = json.load(file)
        for record in records:
            full_name = record["firstName"] + " " + record["lastName"]
            listbox_records.insert(tk.END, full_name)

root = tk.Tk()
root.title("Data Entry")

# First Name
label_first_name = tk.Label(root, text="First Name:")
label_first_name.pack()
entry_first_name = tk.Entry(root)
entry_first_name.pack()

# Last Name
label_last_name = tk.Label(root, text="Last Name:")
label_last_name.pack()
entry_last_name = tk.Entry(root)
entry_last_name.pack()

# Email
label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

# Phone
label_phone = tk.Label(root, text="Phone:")
label_phone.pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

# City
label_city = tk.Label(root, text="City:")
label_city.pack()
entry_city = tk.Entry(root)
entry_city.pack()

# Country
label_country = tk.Label(root, text="Country:")
label_country.pack()
entry_country = tk.Entry(root)
entry_country.pack()

# Profession
label_profession = tk.Label(root, text="Profession:")
label_profession.pack()
entry_profession = tk.Entry(root)
entry_profession.pack()

# Save Button
button_save = tk.Button(root, text="Save Record", command=save_record)
button_save.pack()

# Save to JSON Button
button_save_json = tk.Button(root, text="Save to JSON", command=save_to_json)
button_save_json.pack()

# Show Records Button
button_show_records = tk.Button(root, text="Show Records", command=show_records)
button_show_records.pack()

root.mainloop()