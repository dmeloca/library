import os
import subprocess
import platform

dir_path = r"path/to/your/folder/with/pdfs"

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
            print(f"[!] El libro '{book}' está mal etiquetado")

    return books

def open_pdf(book_name:str):
    try:
        if platform.system() == 'Windows':
            subprocess.run(['start', '', book_name], shell=True)
        else:
            subprocess.run(['open', book_name])
    except FileNotFoundError:
        print("El comando de apertura no está disponible en este sistema.")

def print_library(library:list)-> None:
    counter:int = 1
    for book in library:
        print(f"[{counter}] {especial_print(book.title)}")
        counter += 1

def especial_print(text:str):
    result = ''
    for i, char in enumerate(text):
        if char.isupper() and i != 0:  # Verifica si el carácter es mayúscula y no es el primer carácter
            result += ' ' + char
        else:
            result += char
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
        print("[!] Filtro No encontrado")
        return []
    else:
        parameter = input(f"Ingrese {filters[filter]} del libro: ")
        return tool(library, filters[filter], parameter)
    


def main():
    library = create_library()
    print("Esta es su biblioteca personal")
    while True:
        answer=input("¿Qué desea hacer? (P)rint all titles, (S)earch, (O)pen a book or (E)xit ")
        if answer.lower() == 'p':
            print("Su biblioteca se compone por: ")
            print_library(library)
            exit(0)
        elif answer.lower() == 's':
            search_filter = input("¿Qué filtro desea usar? ((T)itle, (C)ategorie, (D)ate, (E)ditorial, (L)anguage or by (A)uthor)")
            finded_books = search(search_filter.lower(), library)
            print_library(finded_books)
        elif answer.lower() == 'o':
            book_name = input("Ingrese el nombre del libro que desea abrir: ")
            for book in library:
                if book_name == book.title:
                    open_pdf(book.url)
        elif answer.lower() == 'e':
            print("Saliendo")
            exit(0)
        else:
            print("Ingrese un valor correcto")



if __name__ == "__main__":
    main()
