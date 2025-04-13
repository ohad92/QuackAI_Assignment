from app.repository import (
    article_exists,
    insert_article,
    modify_article,
    remove_article,
    find_articles_by_keyword,
    find_articles_by_tag,
    get_all_articles
)

def create_article():
    title = input("Title: ").strip()
    content = input("Content: ").strip()
    tags = input("Tags (comma-separated): ").strip().split(",")

    if not title or not content:
        print("Title and content are required.")
        return

    insert_article(title, content, [tag.strip() for tag in tags if tag.strip()])
    print("Article added successfully.")

def update_article():
    article_id = input("Article ID to edit: ").strip()

    if not article_exists(article_id):
        print(f"Article with ID {article_id} does not exist.")
        return

    field = input("Field to update (title/content/tags): ").strip().lower()

    if field not in ["title", "content", "tags"]:
        print("Invalid field.")
        return

    new_value = input(f"New {field}: ").strip()
    modify_article(article_id, field, new_value)
    print("Article updated.")

def delete_article():
    article_id = input("Article ID to delete: ").strip()

    if not article_exists(article_id):
        print(f"Article with ID {article_id} does not exist.")
        return

    remove_article(article_id)
    print("Article deleted.")

def search_articles():
    option = input("Search by (1) Keyword or (2) Tag: ")
    if option == "1":
        keyword = input("Enter keyword: ").strip()
        results = find_articles_by_keyword(keyword)
    elif option == "2":
        tag = input("Enter tag: ").strip()
        results = find_articles_by_tag(tag)
    else:
        print("Invalid option.")
        return

    for article in results:
        print(article)

def list_articles():
    for article in get_all_articles():
        print(article)