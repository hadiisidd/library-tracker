# library.py
# A simple command-line library tracker.

books = {}  # title -> {"author": str, "available": bool}


def show_menu():
    print("\n=== Library Tracker ===")
    print("0. Exit") 
    print("2. List books")

def list_books():
    if not books:
        print("No books in the library.")
        return

    for title, details in books.items():
        author = details["author"]

        if details["available"]:
            status = "Available"
        else:
            status = "Borrowed"

        print(f"{title} by {author} - {status}")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "2":
            list_books()    
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
