from app.service import (
    create_article,
    update_article,
    delete_article,
    search_articles,
    list_articles
)

def main_menu():
    while True:
        print("\n--- Knowledge Base CLI ---")
        print("1. Add New Article")
        print("2. Edit Article")
        print("3. Delete Article")
        print("4. Search Articles")
        print("5. List All Articles")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_article()
        elif choice == "2":
            update_article()
        elif choice == "3":
            delete_article()
        elif choice == "4":
            search_articles()
        elif choice == "5":
            list_articles()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")