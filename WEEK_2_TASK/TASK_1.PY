# Program to store and display student scores

def main():
    students = {}

    while True:
        print("\n1. Add Student Score")
        print("2. Display All Scores")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            score = int(input("Enter student score: "))
            students[name] = score
            print(f"✅ Score of {name} saved successfully!")

        elif choice == "2":
            if not students:
                print("No student scores available.")
            else:
                print("\n--- Student Scores ---")
                for name, score in students.items():
                    print(f"{name}: {score}")

        elif choice == "3":
            print("Exiting program... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
