import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(root, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(root, textvariable=self.phone_var)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(root, textvariable=self.email_var)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(root, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(root, textvariable=self.address_var)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.contacts_listbox = tk.Listbox(root, width=50)
        self.contacts_listbox.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.search_var = tk.StringVar()
        tk.Label(root, text="Search:").grid(row=6, column=0, padx=5, pady=5)
        self.search_entry = tk.Entry(root, textvariable=self.search_var)
        self.search_entry.grid(row=6, column=1, padx=5, pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        self.display_contacts()

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            self.display_contacts()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields.")

    def display_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")

    def search_contact(self):
        search_term = self.search_var.get().lower()
        results = []
        for contact in self.contacts:
            if search_term in contact["Name"].lower() or search_term in contact["Phone"]:
                results.append(contact)
        self.contacts_listbox.delete(0, tk.END)
        for contact in results:
            self.contacts_listbox.insert(tk.END, f"{contact['Name']}: {contact['Phone']}")

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            selected_contact["Name"] = self.name_var.get()
            selected_contact["Phone"] = self.phone_var.get()
            selected_contact["Email"] = self.email_var.get()
            selected_contact["Address"] = self.address_var.get()
            self.display_contacts()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            confirmed = messagebox.askyesno("Confirm", "Are you sure you want to delete this contact?")
            if confirmed:
                del self.contacts[selected_index[0]]
                self.display_contacts()
                self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def clear_entries(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set("")

root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()
