import json
import re

def main():
    while True:
        articles = read_json()
        print("\n--- Main Menu ---")
        print("1. Add New Article")
        print("2. Edit Article")
        print("3. Delete Article")
        print("4. Search Articles")
        print("5. Print all articles")
        print("6. End")

        user_choise = input("Please choose an option: \n")

        if user_choise == "1":
          add_article(articles)
        elif user_choise == "2":
          edit_article(articles)
        elif user_choise == "3":
          delete_article(articles)
        elif user_choise == "4":
          search_article(articles)
        elif user_choise == "5":
          print_articles(articles)
        elif user_choise == "6":
          print("Program ended")
          break
        else:
          print("Please select from the list above")

def add_article(articles):
  while True:
    article_id = len(articles["articles"]) + 1
    article_title = input("Please write the article title: \n")
    article_content = input("Please write the article content: \n")
    article_tags = list(input("Enter Tags seperated by comma: \n").split(","))
    new_article = {
        "id" : "A" + str(article_id),
        "title" : article_title,
        "content" : article_content,
        "tags" : article_tags
    }
    try:
        articles["articles"].append(new_article)
        write_json(articles)
        print("Article added successfully. \n")
    except Exception as e:
        print(f"Error adding article: {e}")
    break

def edit_article(articles):
    article_id = input("Please choose article to edit (A1\A2\A3...): \n")
    id = find_article(articles,article_id)
    if (id is None):
        print("Article does not exists.")
    else:
        print("Please choose what you want to update:")
        print("1. Title")
        print("2. Content")
        print("3. Tag")
        print("4. End")
        user_option = input()
        if user_option == "1":
            new_title = input("Please write the new title: \n")
            articles["articles"][id]["title"] = new_title
            try:
                write_json(articles)
                print("Title updated successfully. \n")
            except Exception as e:
                print(f"Error updating article: {e}")


        elif user_option == "2":
            new_content = input("Please write the new content: \n")
            articles["articles"][id]["content"] = new_content
            try:
                write_json(articles)
                print("Content updated successfully. \n")
            except Exception as e:
                print(f"Error updating article: {e}")

        elif user_option == "3":
            new_tag = input("Please write the new tag: \n")
            articles["articles"][id]["tags"].append(new_tag)
            try:
                write_json(articles)
                print("Tag added successfully. \n")
            except Exception as e:
                print(f"Error updating article: {e}")

def delete_article(articles):
    article_id = input("Please enter article id to delete (A1\A2\A3..): \n")
    id = find_article(articles,article_id)
    if (id is None):
        print("Article does not exists.")
    else:
        try:
            del articles["articles"][id]
            write_json(articles)
            print ("Article deleted successfully.")
        except Exception as e:
            print(f"Error deleting article: {e}")

def search_article(articles):
    print("Please select the option you want to search: ")
    print("1. Search by keyword")
    print("2. Search by tag")
    user_input = input()
    if user_input == "1":
        keyword = input("Enter keyword \n")
        print("Searching articles by keyword")
        num_of_articles = 0
        for article in articles["articles"]:
            if re.search(r'\b' + re.escape(keyword.lower()) + r'\b', article["title"].lower()) or re.search(
                    r'\b' + re.escape(keyword.lower()) + r'\b', article["content"].lower()):
                print(article)
                num_of_articles +=1
        if num_of_articles == 0:
            print("No articles found")

    elif user_input == "2":
        tag = input("Enter tag: \n")
        print("Searching articles by tag")
        num_of_articles = 0
        for article in articles["articles"]:
            if any(tag.lower() == t.lower() for t in article["tags"]):
                print(article)
                num_of_articles +=1
        if num_of_articles == 0:
            print ("No articles found")

def print_articles(articles):
    for article in articles["articles"]:
        print(article)

def read_json():
  with open('Articles.json') as read_articles:
      load = json.load(read_articles)
      return load

def write_json(articles):
    with open('Articles.json', 'w') as save_file:
        json.dump(articles, save_file, indent=4)

def find_article(articles,article_id):
    for article in articles["articles"]:
        if article["id"] == article_id:
            return articles["articles"].index(article)

if __name__ == "__main__":
    main()
