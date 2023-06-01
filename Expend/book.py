class Book:

    def __init__(self, title, author, number_of_book, subject, number_of_page, add_rack=None):
        self.title = title
        self.author = author
        self.subject = subject
        self.number_of_page = number_of_page
        self.add_rack = add_rack
        self.number_of_book = number_of_book

    def create_book(self):
        self.title = input("\t Enter Name of the Book:")
        self.author = input("\t Enter Name of Author:")
        self.subject = input("\t Enter Category of the Book:")
        self.number_of_page = input("\t Enter Pages of the Book:")
        self.number_of_book = input("\t Enter Number of the Book:")

    def show_book(self):
        print("\t \t Book's ID: ", self.generate_id())
        print("\t \t Book's Name: ", self.title)
        print("\t \t Book's Author: ", self.author)
        print("\t \t Book's Category: ", self.subject)
        print("\t \t Book's Number: ", self.number_of_book)


class Library_Managements:
    count = 0
    
    def __init__(self):
        self.books = []
        self.id = self.generate_id()
        Book.count += 1

    def add_book(self, title, author, subject, number_of_page, number_of_book):
        #Thêm sách
        book = Book(title, author, number_of_book, subject, number_of_page)
        self.books.append(book)

    def generate_id(self):
       # Tạo ID cho sách
        book_id = '{:06d}{:04d}'.format(Book.count, self.number_of_book)
        return book_id

    def display_books(self):
        # Hiển thị danh sách các cuốn sách trong thư viện
        for book in self.books:
            print(
                f"ID: {book.id} | Title: {book.title} | Author: {book.author} | Category: {book.subject} | Number: {book.number_of_book}")


class Search:
    def __init__(self, books):
        self.books = books

    def search_by_title(self, title):
        # Tìm kiếm các cuốn sách có tiêu đề phù hợp
        matching_books = []
        for book in self.books:
            if book.title == title:
                matching_books.append(book)
        return matching_books

    def search_by_author(self, author):
        # Tìm kiếm các cuốn sách có tên tác giả phù hợp
        matching_books = []
        for book in self.books:
            if book.author == author:
                matching_books.append(book)
        return matching_books

    def search_by_subject(self, subject):
        # Tìm kiếm các cuốn sách có danh mục phù hợp
        matching_books = []
        for book in self.books:
            if book.subject == subject:
                matching_books.append(book)
        return matching_books

    @staticmethod
    def display_books(book_list):
        # Hiển thị danh sách các cuốn sách
        for book in book_list:
            print(f"Title: {book.title} | Author: {book.author} | Category: {book.subject}")
