import os
import subprocess
import platform


dir_path = input("Enter the path of the folder where the books are located: ")

class Book:
    def __init__(self, title: str, author: str, date: str, editorial: str, categories: list, language:str, url:str) -> None:
        self.title = title
        self.author = author
        self.date = date
        self.editorial = editorial
        self.categories = categories
        self.laguage = language
        self.url = url
    

def create_library() -> list:
    folder_contents = os.listdir(dir_path)
    library = [book for book in folder_contents if ".pdf" in book]

    books = []

    for book in library:
        book_url = book
        book = book.replace('.pdf', '')
        book_info = book.split('_')
        
        try:
            new_book = Book(title=book_info[2], author=book_info[0], date=book_info[1], editorial=book_info[5], categories=book_info[3].split("#"), language=book_info[4], url=book_url)
            books.append(new_book)

        except IndexError:
            print(f"[!] The book '{book}' is not well formatted.")

    return books

def open_pdf(book_name:str):
    try:
        if platform.system() == 'Windows':
            book_name = os.path.join(dir_path, book_name)
            subprocess.run(['start', '', book_name], shell=True)
        else:
            subprocess.run(['open', book_name])
    except FileNotFoundError:
        print("The open command is not available.")

def print_library(library:list)-> None:
    counter:int = 1
    for book in library:
        if counter < 10:
            zero_counter = f"0{counter}"
            print(f"[{zero_counter}] {especial_print(book.title)}")
        else:
            print(f"[{counter}] {especial_print(book.title)}")
        counter += 1

def especial_print(text:str):
    result = text.replace('-', ' ')
    return result

def tool(library:list, filter:str, parameter:str):
    result = []
    for book in library:
        if parameter in getattr(book, filter):
            result.append(book)
    return result

def search(filter:str, library:list) -> list:
    filters = {'a': 'author', 'd': 'date', 't': 'title', 'c': 'categories', 'l': 'language', 'e': 'editorial'}
    if filter not in filters:
        print("[!] Filter not found.")
        return []
    else:
        parameter = input(f"Enter the {filters[filter]} of the book: ")
        return tool(library, filters[filter], parameter)
    


def main():
    library = create_library()
    print("This is your bookshelf, enjoy it!")
    while True:
        answer=input("What do you want to do? (P)rint all titles, (S)earch, (O)pen a book or (E)xit ")
        if answer.lower() == 'p':
            print("Your bookshelf: ")
            print_library(library)
        elif answer.lower() == 's':
            search_filter = input("Which filter do you want to use? ((T)itle, (C)ategorie, (D)ate, (E)ditorial, (L)anguage or by (A)uthor)")
            finded_books = search(search_filter.lower(), library)
            print_library(finded_books)
        elif answer.lower() == 'o':
            book_name = input("Enter the name of the book you want to open:")
            for book in library:
                if book_name == book.title:
                    open_pdf(book.url)
        elif answer.lower() == 'e':
            print("Goodbye!")
            exit(0)
        else:
            print("Please enter a valid option.")



if __name__ == "__main__":
    main()
