
class book:
    def __init__(self, ID=" ", book_name=" ", category=" ", price=" ", remain=" "):
        self.ID = ID
        self.book_name = book_name
        self.category = category
        self.price = price
        self.remain = remain
        self.book_list = {}
        self.book_lend = {}

    def create_book(self):

        self.ID = input("\t Enter Book Number:")
        self.book_name = input("\t Enter Name of the Book:")
        self.category = input("\t Enter Name of the Category:")
        self.price = input("\t Enter Price of the Book:")
        self.remain = input("\t Enter Remain of the Book:")

    def show_book(self):

        print("\t \t Book Number: ", self.ID)

        print("\t \t Book Name: ", self.book_name)

        print("\t \t Category Name: ", self.category)

        print("\t \t Price: ", self.price)

        print("\t \t Remain: ", self.remain)

    def modify_book(self):

        print("\t \t Book No.: ", self.ID)

        self.book_name = input("\t \t Enter New Book Name: ")

        self.category = input("\t \t Enter New Category Name:")

        self.price = input("\t \t Enter New Price:")

        print("\t \t Book Modified")

    def ret_id(self):
        return self.ID

    def report_book(self):
        print(self.ID, self.book_name, self.category, self.price)

    def addBook(self, book_name):
        self.book_list.append(book_name)
        print("Book has been added")

    def lend(self):
        book_name = input("Enter the book name\n")
        if book_name in self.book_list.keys():
            print(f"The book you are searching for is with {self.book_list[book_name]}")
        else:
            print("My library don't have this book")

    def return_book(self):
        book_name = input("Enter the book name that you want to return\n")
        tempName = self.book_list[book_name]
        self.book_list.pop(book_name)
        print(f"Thankyou for returning the book {tempName}")
