from app.controller import main_menu
from app.db import initialize_db

if __name__ == "__main__":
    initialize_db()
    main_menu()