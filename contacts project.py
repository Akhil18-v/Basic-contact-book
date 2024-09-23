def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts.append((name, phone))
    print("Contact added!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("Your contacts:")
        for index, (name, phone) in enumerate(contacts):
            print(f"{index + 1}. {name} - {phone}")

def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed_contact = contacts.pop(index)
            print(f"Contact '{removed_contact[0]}' removed!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    filename = 'contacts.txt'
    contacts = load_contacts(filename)

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            save_contacts(filename, contacts)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()