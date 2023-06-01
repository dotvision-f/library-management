from openpyxl import Workbook
from openpyxl import load_workbook
import os

from UI import *
from member_db import *
from book_db import *
from Expend.book import *

class Build:
    def __init__(self):
        # Load Member
        self.Member_DB = Member_DB()
        self.Member_DB.write_header()
        self.Member_DB.add_member('admin', 'admin', 11111111, 'Admin',3)
        self.Member_DB.add_member('teacher@phenikaa-uni.edu.vn', 2023, 20002000, 'Teacher 1')
        self.Member_DB.add_member('20010737@st.phenikaa-uni.edu.vn', 2023, 20010737, 'Tran Van Do')
        self.Member_DB.add_member('20010738@st.phenikaa-uni.edu.vn', 2023, 20010738, 'Le Quan Dung')
        self.Member_DB.add_member('20010753@st.phenikaa-uni.edu.vn', 2023, 20010753, 'Nguyen Ngoc Tu')
        self.Member_DB.add_member('20010735@st.phenikaa-uni.edu.vn', 2023, 20010735, 'Nguyen Duy Anh')
        self.Member_DB.add_member('1', 2, 20010735, 'Nguyen Duy Anh', in_bag="book1")
        self.Member_DB.save_db()
        # Load Book
        self.Book_DB = Book_DB()
        self.Book_DB.write_header()
        self.Book_DB.add_book('book1', "Author1", 'Sbj1, Sbj2', './pdf/book1.pdf')
        self.Book_DB.add_book('book2', "Author2", 'Sbj2', './pdf/book2.pdf')
        self.Book_DB.add_book('book3', "Author3", 'Sbj3, Sbj2', './pdf/book3.pdf')
        self.Book_DB.save_db()

        self.list_book = []
        self.info_book = {}
        self.name_type = 'Title'
    def reload_db(self):
        self.member_db = self.Member_DB.sheet
        self.book_db = self.Book_DB.sheet

    def Func_Home(self):
        home = Home()
        self.reload_db()
        if home == "1":
            self.username = Username()
            row_index = self.Member_DB.find_row_index(self.username)
            if row_index is not None:
                password = Password_4P(self.username, self.member_db[f"B{row_index}"].value)
                if password == self.member_db[f"B{row_index}"].value:
                    if self.member_db[f"C{row_index}"].value == 3:
                        self.Func_Main_Admin()
                    else:
                        self.Func_Main_Member()
                else:
                    Forget_password(self.username)
                    self.Func_Home()
            else:
                password = Creat_password(self.username)
                ### Them vao database: self.username, password
                self.Member_DB.add_member(self.username, password)
                Done_sign_up()
                self.Func_Home()
        else:
            pass

    def Func_Main_Member(self):
        main = Main(self.username)
        if main == "1":
            self.Func_Read_borrow_book()
        elif main == "2":
            self.Func_Personal_information()
        else:
            self.Func_Home()
    ##
    def Func_Read_borrow_book(self):
        read_borrow_book = Read_borrow_book()
        if read_borrow_book == "1":
            self.Func_Your_book_list()
        elif read_borrow_book == "2":
            self.Func_search("Title")
        elif read_borrow_book == "3":
            self.Func_search("Author")
        elif read_borrow_book == "4":
            self.Func_search("Subject")
        else:
            self.Func_Main_Member()
    ###
    def Func_Your_book_list(self):
        your_book_list = Your_book_list()
        # self.list_book = ['book1', 'book2'] #####
        row_index = self.Member_DB.find_row_index(self.username)
        (email, password, level, in_bag, id, name) = list(self.member_db.rows)[row_index-1]
        self.mem_list_book = in_bag.value.split(",")[1:]
        if your_book_list == "1":
            self.Func_Your_online_book_list()
        elif your_book_list == "2":
            self.Func_Your_offline_book_list()
        elif your_book_list == "00":
            self.Func_Read_borrow_book()
        else:
            self.Func_Main_Member()
    ####
    def Func_Your_online_book_list(self, back='book'):
        your_online_book_list = Your_online_book_list(self.mem_list_book)
        if your_online_book_list == "00":
            if back == 'book': self.Func_Your_book_list()()
            else: self.Func_Personal_information()
        elif your_online_book_list == "0":
            self.Func_Main_Member()
        else:
            row_index = self.Book_DB.find_row_index(self.mem_list_book[int(your_online_book_list)-1])
            (title, author, subject, PDF_link) = list(self.book_db.rows)[row_index-1]
            self.info_book = {"title": title.value, "author": author.value,\
                              "subject": subject.value, "PDF_link":PDF_link.value}
            self.Func_Online_choose_book()
    #####
    def Func_Online_choose_book(self):
        online_choose_book = Online_choose_book(self.info_book)
        if online_choose_book == "1":
            self.Func_Read_book()
        elif online_choose_book == "2":
            ##### Checking
            self.Func_Download_pdf_file()
        elif online_choose_book == "3":
            ##### Remove from data base
            self.mem_list_book.remove(self.info_book['title'])
            row_index = self.Member_DB.find_row_index(self.username)
            self.member_db[f'D{row_index}'].value = ""
            for book in self.mem_list_book:
                self.member_db[f'D{row_index}'].value += f",{book}"
            Remove_from_list(self.info_book)
            self.Func_Main_Member()
        elif online_choose_book == "00":
            self.Func_Your_online_book_list()
        else:
            self.Func_Main_Member()
    ######
    def Func_Read_book(self):
        os.system(f"open {self.info_book['PDF_link']}")
        read_book = Read_book(self.info_book)
        if read_book == "00":
            self.Func_Online_choose_book()
        else:
            self.Func_Main_Member()
    ######
    def Func_Download_pdf_file(self):
        download_pdf_file = Download_pdf_file(self.info_book)
        if download_pdf_file == "00":
            self.Func_Online_choose_book()
        else:
            self.Func_Main_Member()
    ####
    def Func_Your_offline_book_list(self, back='book'):
        self.mem_list_book = []
        your_offline_book_list = Your_offline_book_list(self.mem_list_book)
        if your_offline_book_list == "00":
            if back == 'book': self.Func_Your_book_list()()
            else: self.Func_Personal_information()
        elif your_offline_book_list == "0":
            self.Func_Main_Member()
        else:
            self.Func_Offline_choose_book()
    #####
    def Func_Offline_choose_book(self):
        offline_choose_book = Offline_choose_book(self.info_book)
        if offline_choose_book == "1":
            self.Func_Return_book()
        elif offline_choose_book == "00":
            self.Func_Your_offline_book_list()
        else:
            self.Func_Main_Member()
    ######
    def Func_Return_book(self):
        return_book = Return_book(self.info_book)
        if return_book == "00":
            self.Func_Offline_choose_book()
        else:
            self.Func_Main_Member()

    ###
    def Func_search(self, name_type):
        self.name_type = name_type
        if self.name_type == "Title":
            self.List_search = Title_list_search
        elif self.name_type == "Author":
            self.List_search = Author_list_search
        elif self.name_type == "Subject":
            self.List_search = Subject_list_search
        
        self.type_of_search = Type_of_search(self.name_type) # Nhập title
        if self.type_of_search == "00":
            self.Func_Read_borrow_book()
        elif self.type_of_search == "0":
            self.Func_Main_Member()
        else:
            if self.name_type == "Title":
                self.list_book = self.Book_DB.search_book_title(self.type_of_search)
            elif self.name_type == "Author":
                self.list_book = self.Book_DB.search_book_author(self.type_of_search)
            elif self.name_type == "Subject":
                self.list_book = self.Book_DB.search_book_subject(self.type_of_search)
            self.Func_List_search()
    ####
    def Func_List_search(self):
        list_search = self.List_search(self.type_of_search, self.list_book)
        if list_search == "00":
            self.Func_search(self.name_type)
        elif list_search == "0":
            self.Func_Main_Member()
        else:
            row_index = self.Book_DB.find_row_index(self.list_book[int(list_search)-1])
            (title, author, subject, PDF_link) = list(self.book_db.rows)[row_index-1]
            self.info_book = {"title": title.value, "author": author.value,\
                              "subject": subject.value, "PDF_link":PDF_link.value}
            self.Func_Choose_book()
    #####
    def Func_Choose_book(self):
        choose_book = Choose_book(self.info_book)
        if choose_book == "1":
            self.Func_Read_book()
        elif choose_book == "2":
            self.Func_Borrow_book()
        elif choose_book == "3":
            ##### checking
            self.Func_Download_pdf_file()
        elif choose_book == "00":
            self.Func_List_search()
        else:
            self.Func_Main_Member()
    ######
    def Func_Borrow_book(self):
        self.Member_DB.add_to_bag(self.username, self.info_book['title'])
        borrow_book = Borrow_book(self.info_book)
        if borrow_book == "00":
            self.Func_Choose_book()
        else:
            self.Func_Main_Member()

    ##
    def Func_Personal_information(self):
        # self.info_member = {"name": "x", "age": 20} ##### Member.get_info()
        row_index = self.Member_DB.find_row_index(self.username)
        (email, password, level, in_bag, id, name) = list(self.member_db.rows)[row_index-1]
        self.info_member = {"name":name.value, "email":email.value, "level":level.value,\
                            "Book in bag":in_bag.value, "id":id.value}
        personal_info = Personal_info(self.info_member)
        if personal_info == "1":
            self.Func_Your_online_book_list(back='')
        elif personal_info == "2":
            self.Func_Your_offline_book_list(back='')
        elif personal_info == "3":
            self.Func_Edit_info_member()
        else:
            self.Func_Main_Member()
    ###
    def Func_Edit_info_member(self, back=""):
        self.edit_info_member = Edit_info_member(self.info_member)
        if self.edit_info_member == "00":
            self.Func_Personal_information()
        elif self.edit_info_member == "0":
            if back == "admin": self.Func_Main_Admin()
            else: self.Func_Main_Member()
        else:
            self.Func_Object_edit_info_member()
    ####
    def Func_Object_edit_info_member(self):
        self.object_edit_info_member = Object_edit_info_member(self.edit_info_member)
        if self.object_edit_info_member == "00":
            self.Func_Edit_info_member()
        elif self.object_edit_info_member == "0":
            self.Func_Main_Member()
        else:
            self.Func_Done_edit_info_member()

    #####
    def Func_Done_edit_info_member(self):
        self.Member_DB.change_info(self.username,self.edit_info_member, self.object_edit_info_member)
        done_edit_info_member = Done_edit_info_member(self.edit_info_member)
        if done_edit_info_member == "00":
            self.Func_Edit_info_member()
        else:
            self.Func_Main_Member()

    
    ################################
    #
    def Func_Main_Admin(self):
        main_admin = Main_admin()
        if main_admin == "1":
            self.Func_Manage_member()
        elif main_admin == "2":
            self.Func_Manage_book()
        else:
            self.Func_Home()
    ##
    def Func_Manage_member(self):
        manage_member = Manage_member()
        if manage_member == "1":
            self.Func_Overview_member()
        elif manage_member == "2":
            self.Func_Detail_member()
        else:
            self.Func_Main_Admin()
    ###
    def Func_Overview_member(self):
        guests = 0
        students = 0
        teachers = 0
        for i in range(self.Member_DB.count):
            if self.member_db[f"C{i+1}"].value == 0: guests +=1
            elif self.member_db[f"C{i+1}"].value == 1: students +=1
            elif self.member_db[f"C{i+1}"].value == 2: teachers +=1
        overview_member = Overview_member(guests, students, teachers)
        if overview_member == "00":
            self.Func_Manage_member()
        else:
            self.Func_Main_Admin()
    
    ###
    def Func_Detail_member(self):
        self.list_member = []
        for i in range(1,self.Member_DB.count):
            self.list_member.append(self.member_db[f"A{i+1}"].value)
        detail_member = Detail_member(self.list_member)
        if detail_member == "00":
            self.Func_Manage_member()
        elif detail_member == "0":
            self.Func_Main_Admin()
        else:
            # self.info_member = {"name": "x", "age": 20, 'status':'ACTIVE'} #####
            row_index = self.Member_DB.find_row_index(self.list_member[int(detail_member)-1])
            (email, password, level, in_bag, id, name) = list(self.member_db.rows)[row_index-1]
            self.info_member = {"name":name.value, "email":email.value, "level":level.value,\
                                "Book in bag":in_bag.value, "id":id.value}
            self.mem_list_book = in_bag.value.split(",")[1:]
            self.Func_Choose_member()
    
    ####
    def Func_Choose_member(self):
        choose_member = Choose_member(self.info_member)
        if choose_member == "1":
            self.Func_Edit_info_member(back="admin")
        elif choose_member == "2":
            self.Func_Books_of_member()
        elif choose_member == "3":
            self.Func_Remove_member()
        elif choose_member == "00":
            self.Func_Detail_member()
        else:
            self.Func_Main_Admin()
    
    #####
    def Func_Books_of_member(self):
        books_of_member = Books_of_member(self.info_member['name'], self.mem_list_book)
        if books_of_member == "00":
            self.Func_Choose_member()
        else:
            self.Func_Main_Admin()
    
    #####
    def Func_Remove_member(self):
        self.Member_DB.remove_member(self.info_member['email'])
        remove_member = Remove_member(self.info_member)
        if remove_member == "00":
            self.Func_Choose_member()
        else:
            self.Func_Main_Admin()
    
    ##
    def Func_Manage_book(self):
        manage_book = Manage_book()
        if manage_book == "1":
            self.Func_Overview_book()
        elif manage_book == "2":
            self.Func_Detail_book()
        elif manage_book == "3":
            self.Func_Add_book()
        else:
            self.Func_Main_Admin()
    ###
    def Func_Overview_book(self):
        overview_book = Overview_book(self.Book_DB.count-1)
        if overview_book == "00":
            self.Func_Manage_book()
        else:
            self.Func_Main_Admin()
    
    ###
    def Func_Detail_book(self):
        # self.list_book = ['book1', 'book2'] ######
        self.list_book = []
        for i in range(1,self.Book_DB.count):
            self.list_book.append(self.book_db[f"A{i+1}"].value)
        detail_book = Detail_book(self.list_book)
        if detail_book == "00":
            self.Func_Manage_book()
        elif detail_book == "0":
            self.Func_Main_Admin()
        else:
            # self.info_book = {"title": "x", "author": "z"} #####
            row_index = self.Book_DB.find_row_index(self.list_book[int(detail_book)-1])
            (title, author, subject, PDF_link) = list(self.book_db.rows)[row_index-1]
            self.info_book = {"title": title.value, "author": author.value,\
                    "subject": subject.value, "PDF_link":PDF_link.value}
            self.Func_Choose_book_admin()
    
    ####
    def Func_Choose_book_admin(self):
        choose_book = Choose_book_admin(self.info_book)
        if choose_book == "1":
            self.Func_Edit_info_book()
        elif choose_book == "2":
            self.Func_Remove_book()
        elif choose_book == "00":
            self.Func_Detail_book()
        else:
            self.Func_Main_Admin()
    
    #####
    def Func_Edit_info_book(self):
        self.edit_info_book = Edit_info_book(self.info_book)
        if self.edit_info_book == "00":
            self.Func_Choose_book_admin()
        elif self.edit_info_book == "0":
            self.Func_Main_Admin()
        else:
            self.Func_Object_edit_info_book()
    ####
    def Func_Object_edit_info_book(self):
        self.object_edit_info_book = Object_edit_info_book(self.edit_info_book)
        if self.object_edit_info_book == "00":
            self.Func_Edit_info_book()
        elif self.object_edit_info_book == "0":
            self.Func_Main_Admin()
        else:
            self.Func_Done_edit_info_book()

    #####
    def Func_Done_edit_info_book(self):
        self.Book_DB.change_info(self.info_book['title'],self.edit_info_book, self.object_edit_info_book)
        done_edit_info_book = Done_edit_info_book(self.edit_info_book)
        if done_edit_info_book == "00":
            self.Func_Edit_info_book()
        else:
            self.Func_Main_Admin()


    #####
    def Func_Remove_book(self):
        self.Book_DB.remove_book(self.info_book['title'])
        remove_book = Remove_book(self.info_book)
        if remove_book == "00":
            self.Func_Choose_book()
        else:
            self.Func_Main_Admin()
    ###
    def Func_Add_book(self):
        book = Add_book()
        self.Book_DB.add_book(book['title'], book['author'], book['subject'], book['PDF_link'])
        done_add_book = Done_add_book(book)
        if done_add_book == "00":
            self.Func_Manage_book()
        else:
            self.Func_Main_Admin()
    
    def __call__(self):
        return self.Func_Home()

run = Build()
run()

    

