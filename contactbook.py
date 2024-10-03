class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address): 
        contact = Contact(name, phone, email, address)  # Corrected variable name
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("Contact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]

        if results:
            print("Search Results:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("No contacts found.")

    def update_contact(self, name, phone=None, email=None, address=None):  # Added email parameter
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if phone:
                    contact.phone = phone
                if email:
                    contact.email = email  # Fixed missing email assignment
                if address:
                    contact.address = address
                print(f"Contact {name} updated successfully.")
                return
        print(f"Contact {name} not found.")  # Moved outside the loop

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")  # Moved outside the loop


def main():  # Added missing colon
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter name: ")  # Fixed typo
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            contact_book.update_contact(name, phone if phone else None, email if email else None, address if address else None)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
