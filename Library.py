class Library:
    def __init__(self):
        self.books_by_id = {}
        self.books_by_title = {}
        self.books_by_author = {}

    def add_book(self, book_id, title, authors, genre, publication_year):
        self.books_by_id[book_id] = {
            "Title": title,
            "Authors": authors,
            "Genre": genre,
            "Publication Year": publication_year
        }

        self.books_by_title[title] = book_id

        for author in authors:
            if author not in self.books_by_author:
                self.books_by_author[author] = []
            self.books_by_author[author].append(book_id)

    def find_by_title(self, title):
        book_id = self.books_by_title.get(title)
        if book_id:
            return self.books_by_id[book_id]
        return "Book not found."

    def find_by_author(self, author):
        book_ids = self.books_by_author.get(author, [])
        return [self.books_by_id[book_id] for book_id in book_ids] if book_ids else "No books found by this author."





# library = Library()
# library.add_book(1, "Book1", ["Author1"], "Fiction", 2020)
# library.add_book(2, "Book2", ["Author2"], "Non-Fiction", 2018)
# library.add_book(3, "Book3", ["Author1", "Author3"], "Fiction", 2021)
# print("Find by title:", library.find_by_title("Book1"))
# print("Find by author:", library.find_by_author("Author1"))
# print("Find by author:", library.find_by_author("Author4"))
