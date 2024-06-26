# Bookshelf Manager

Bookshelf Manager is a simple Python script to manage your PDF book collection. It organizes books based on metadata embedded in the file names and allows you to search, list, and open books directly from the command line.

## Features

- Organizes books by author, date, title, categories, language, and editorial.
- Lists all books in your collection.
- Allows searching books by various metadata fields.
- Opens books directly from the command line.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/dmeloca/bookshelf-manager.git
    cd bookshelf-manager
    ```

2. **Dependencies**: This project does not have any external dependencies outside of the Python standard library.

## Usage

1. **Run the script**:
    ```bash
    python main.py
    ```

2. **Follow the prompts** to enter the path of the folder where your books are located.

3. **Commands**:
    - `(P)rint all titles`: Lists all books in your collection.
    - `(S)earch`: Allows you to search books by title, categories, date, editorial, language, or author.
    - `(O)pen a book`: Opens a specified book. (For now only works on Windows)
    - `(E)xit`: Exits the program.

## Book Naming Format

The script expects books to be named in a specific format to extract metadata:
`author_date_title_#categorie1#categorie2_language_editorial.pdf`


### Example
`doe_2023_my-book_fiction#fantasy_english_penguin.pdf`


## Contributing

Contributions are welcome! Please open an issue to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- Daniel Melo - Initial work - [dmeloca](https://github.com/dmeloca)


