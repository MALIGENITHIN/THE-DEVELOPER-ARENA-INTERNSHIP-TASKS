import os

FILE_NAME = "contact_book.txt"

def save_entry(name, phone, email, notes=""):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email},{notes}\n")
    print("✅ Entry saved successfully!\n")

def view_entries():
    if not os.path.exists(FILE_NAME):
        print("No entries found.\n")
        return
    with open(FILE_NAME, "r") as file:
        entries = file.readlines()
        if not entries:
            print("No entries found.\n")
            return
        print("📖 Saved Entries:")
        for i, entry in enumerate(entries, start=1):
            name, phone, email, notes = entry.strip().split(",", 3)
            print(f"{i}. Name: {name}, Phone: {phone}, Email: {email}, Notes: {notes}")

def search_entry(keyword):
    if not os.path.exists(FILE_NAME):
        print("No entries to search.\n")
        return
    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            if keyword.lower() in line.lower():
                name, phone, email, notes = line.strip().split(",", 3)
                print(f"🔍 Found: Name: {name}, Phone: {phone}, Email: {email}, Notes: {notes}")
                found = True
    if not found:
        print("❌ No matching entry found.\n")

def main():
    while True:
        print("\n===== Contact Book / Journal =====")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Search Entry")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            notes = input("Enter notes (optional): ")
            save_entry(name, phone, email, notes)
        elif choice == "2":
            view_entries()
        elif choice == "3":
            keyword = input("Enter name/phone/email to search: ")
            search_entry(keyword)
        elif choice == "4":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
