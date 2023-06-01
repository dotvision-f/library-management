from UI import *

class Build:
    def __init__(self):
        self.list_book = []
        self.info_book = {}
        self.name_type = 'Title'
        self.databases = [{"username": "1", "password": "2", "type": "member"},\
                          {"username": "11", "password": "22", "type": "admin"}]

    def Func_Home(self):
        home = Home()
        if home == "1":
            self.username = Username()
            isTrue_username = False
            for database in self.databases:
                if self.username == database["username"]:
                    isTrue_username = True
                    password = Password_4P(self.username, database["password"])
                    if password == database["password"]:
                        if database["type"] == "admin":
                            self.Func_Main_Admin()
                        else:
                            self.Func_Main_Member()
                    else:
                        Forget_password(self.username)
                        self.Func_Home()
                else:
                    continue
            if not isTrue_username:
                password = Creat_password(self.username)
                ### Them vao database: self.username, password
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
        self.list_book = ['book1', 'book2'] #####
        if your_book_list == "1":
            self.Func_Your_online_book_list()
        elif your_book_list == "2":
            self.Func_Your_offline_book_list(self.list_book)
        elif your_book_list == "00":
            self.Func_Read_borrow_book()
        else:
            self.Func_Main_Member()
    ####
    def Func_Your_online_book_list(self, back='book'):
        your_online_book_list = Your_online_book_list(self.list_book)
        if your_online_book_list == "00":
            if back == 'book': self.Func_Your_book_list()()
            else: self.Func_Personal_information()
        elif your_online_book_list == "0":
            self.Func_Main_Member()
        else:
            self.info_book = {"title": "x", "author":"b"} #####
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
            Remove_from_list(self.info_book)
            self.Func_Main_Member()
        elif online_choose_book == "00":
            self.Func_Your_online_book_list()
        else:
            self.Func_Main_Member()
    ######
    def Func_Read_book(self):
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
        your_offline_book_list = Your_offline_book_list(self.list_book)
        if your_offline_book_list == "00":
            if back == 'book': self.Func_Your_book_list()()
            else: self.Func_Personal_information()
        elif your_offline_book_list == "0":
            self.Func_Main_Member()
        else:
            self.info_book = {"title": "x", "author":"b"} #####
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
        return_book = Return_book(self.info_book)   ##### Creat random number (4 chữ số) để admin check
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
            self.list_book = ['book1', 'book2'] ######
            self.Func_List_search()
    ####
    def Func_List_search(self):
        list_search = self.List_search(self.type_of_search, self.list_book)
        if list_search == "00":
            self.Func_search(self.name_type)
        elif list_search == "0":
            self.Func_Main_Member()
        else:
            self.info_book = {"title": "x", "author":"b"} #####
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
        borrow_book = Borrow_book(self.info_book)
        if borrow_book == "00":
            self.Func_Choose_book()
        else:
            self.Func_Main_Member()

    ##
    def Func_Personal_information(self):
        self.info_member = {"name": "x", "age": 20}
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
    def Func_Edit_info_member(self):
        self.edit_info_member = Edit_info_member(self.info_member)
        if self.edit_info_member == "00":
            self.Func_Personal_information()
        elif self.edit_info_member == "0":
            self.Func_Main_Member()
        else:
            self.Func_Object_edit_info_member()
    ####
    def Func_Object_edit_info_member(self):
        object_edit_info_member = Object_edit_info_member(self.edit_info_member)
        if object_edit_info_member == "00":
            self.Func_Edit_info_member()
        elif object_edit_info_member == "0":
            self.Func_Main_Member()
        else:
            self.Func_Done_edit_info_member()

    #####
    def Func_Done_edit_info_member(self):
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
        overview_member = Overview_member()
        if overview_member == "00":
            self.Func_Manage_member()
        else:
            self.Func_Main_Admin()
    
    ###
    def Func_Detail_member(self):
        self.list_member = ['p1', 'p2'] ######
        detail_member = Detail_member(self.list_member)
        if detail_member == "00":
            self.Func_Manage_member()
        elif detail_member == "0":
            self.Func_Main_Admin()
        else:
            self.info_member = {"name": "x", "age": 20, 'status':'ACTIVE'} #####
            self.Func_Choose_member()
    
    ####
    def Func_Choose_member(self):
        choose_member = Choose_member(self.info_member)
        if choose_member == "1":
            self.Func_Edit_info_member()
        elif choose_member == "2":
            self.Func_Books_of_member()
        elif choose_member == "3":
            self.Func_Block_member()
        elif choose_member == "4":
            self.Func_Active_member()
        elif choose_member == "00":
            self.Func_Detail_member()
        else:
            self.Func_Main_Admin()
    
    #####
    def Func_Books_of_member(self):
        books_of_member = Books_of_member(self.info_member)
        if books_of_member == "00":
            self.Func_Choose_member()
        else:
            self.Func_Main_Admin()
    
    #####
    def Func_Block_member(self):
        block_member = Block_member(self.info_member)
        if block_member == "00":
            self.Func_Choose_member()
        else:
            self.Func_Main_Admin()

    #####
    def Func_Active_member(self):
        active_member = Active_member(self.info_member)
        if active_member == "00":
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
        overview_book = Overview_book()
        if overview_book == "00":
            self.Func_Manage_book()
        else:
            self.Func_Main_Admin()
    
    ###
    def Func_Detail_book(self):
        self.list_book = ['book1', 'book2'] ######
        detail_book = Detail_book(self.list_book)
        if detail_book == "00":
            self.Func_Manage_book()
        elif detail_book == "0":
            self.Func_Main_Admin()
        else:
            self.info_book = {"title": "x", "author": "z"} #####
            self.Func_Choose_book_admin()
    
    ####
    def Func_Choose_book_admin(self):
        choose_book = Choose_book(self.info_book)
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
            self.Func_book_information()
        elif self.edit_info_book == "0":
            self.Func_Main_Admin()
        else:
            self.Func_Object_edit_info_book()
    ####
    def Func_Object_edit_info_book(self):
        object_edit_info_book = Object_edit_info_book(self.edit_info_book)
        if object_edit_info_book == "00":
            self.Func_Edit_info_book()
        elif object_edit_info_book == "0":
            self.Func_Main_Admin()
        else:
            self.Func_Done_edit_info_book()

    #####
    def Func_Done_edit_info_book(self):
        done_edit_info_book = Done_edit_info_book(self.edit_info_book)
        if done_edit_info_book == "00":
            self.Func_Edit_info_book()
        else:
            self.Func_Main_Admin()


    #####
    def Func_Remove_book(self):
        remove_book = Remove_book(self.info_book)
        if remove_book == "00":
            self.Func_Choose_book()
        else:
            self.Func_Main_Admin()
    ###
    def Func_Add_book(self):
        add_book = Add_book()
        # code add book
        done_add_book = Done_add_book(add_book)
        if done_add_book == "00":
            self.Func_Manage_book()
        else:
            self.Func_Main_Admin()
    
    def __call__(self):
        return self.Func_Home()

run = Build()
run()

    

