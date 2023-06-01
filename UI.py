from gui import *
import os
import functools
import operator

databases = [{"username": "1", "password": "2", "type": "member"},\
                          {"username": "11", "password": "22", "type": "admin"}]

# Man hinh chao don ban dau
## Dang nhap va dang ky cung chung man hinh.

def show_fix(gui: gui, syntaxs: list, fix='number', back=""):
    if back != "read":
        os.system('clear')
    if fix == 'password': x1 = "password"
    else: x1 = 'number/syntax'
    print(gui)
    res = input(f"Enter the {fix}: ")
    while True:
        if res not in syntaxs:
            res = input(f"--- Wrong {x1}, re-enter the {fix}: ")
        else: break
    return res

def show_content(title, lists, fix='syntax/number', type_syntax = "number"):
    os.system('clear')
    print(gui.Title(title))
    if type_syntax == "number":
        syntaxs = functools.reduce(operator.iconcat, [["0","00"], [str(i) for i in range(1,len(lists)+1)]], [])
        for i in range(len(lists)):
            print(f"{i+1}. {lists[i]}")
    else:
        syntaxs = functools.reduce(operator.iconcat, [["0","00"], lists.keys()], [])
        for i in lists:
            print(f"{i}: {lists[i]}")
    print('''
Enter the syntax/number OR

0. trở về home page
00. trở về trang trước
''')
    res = input(f"Enter the {fix}: ")
    while True:
        if res not in syntaxs:
            res = input(f"--- Wrong {fix}, re-enter the {fix}: ")
        else: break
    return res

def Home():
    return show_fix(gui.home, ["1", "2"], 'number')

def Username():
    os.system('clear')
    print(gui.username)
    username = input("Username or Email: ")
    return username

def Password_4P(username, password):
    # lists = functools.reduce(operator.iconcat, ["1", password], [])
    return show_fix(gui.Password_4P(username),["1",password], 'password')

def Forget_password(username):
    return show_fix(gui.Forget_password(username), ["0"])

def Creat_password(username):
    os.system('clear')
    print(gui.Password_1(username))
    password_1 = input("Enter new password: ")
    password_2 = input("Re-enter the password: ")
    while True:
        if password_1 != password_2:
            print("--- Two passwords aren't the same, enter the new pasword.")
            password_1 = input("Enter new password: ")
            password_2 = input("Re-enter the password: ")
        else: break
    return password_1

def Done_sign_up():
    return show_fix(gui.done_sign_up, ["0"])

################### Sign In Success ##################
def Main(username):
    return show_fix(gui.Main(username), ["1", "2", "3"])

def Read_borrow_book():
    return show_fix(gui.read_borrow_book, ["1","2","3", "4","00", "0"])

def Your_book_list():
    return show_fix(gui.your_book_list, ["1","2","0","00"])

def Your_online_book_list(list_book:list):
    return show_content('Your online book list', list_book)

def Online_choose_book(info_book:dict):
    return show_fix(gui.Online_choose_book(info_book), ["1", "2", "3", "0", "00"])

def Read_book(info_book:dict):
    return show_fix(gui.Read_book(info_book), ["0","00"], back="read")

def Download_pdf_file(info_book:dict):
    return show_fix(gui.Download_pdf_file(info_book), ["0","00"])

def Remove_from_list(info_book:dict):
    return show_fix(gui.Remove_from_list(info_book), ["0"])

def Your_offline_book_list(list_book:list):
    return show_content('Your online book list', list_book)

def Offline_choose_book(info_book:dict):
    return show_fix(gui.Office_choose_book(info_book), ["1", "0", "00"])

def Return_book(info_book:dict):
    return show_fix(gui.Return_book(info_book), ["0", "00"])

def Search_by_title():
    os.system('clear')
    print(gui.search_by_title)
    search_by_title = input("Enter the title: ")
    return search_by_title

def Title_list_search(str_search:str, list_search:list):
    return show_content(f"Search by Title: {str_search}", list_search)

def Author_list_search(str_search:str, list_search:list):
    return show_content(f"Search by Author: {str_search}", list_search)

def Subject_list_search(str_search:str, list_search:list):
    return show_content(f"Search by Subject: {str_search}", list_search)

def Type_of_search(name_type:str):
    os.system('clear')
    print(gui.Type_of_search(name_type))
    type_of_search = input(f"Enter the {name_type}: ")
    return type_of_search

def Choose_book(info_book:dict):
    return show_fix(gui.Choose_book(info_book), ["1","2","3","0","00"])

def Borrow_book(info_book:dict):
    return show_fix(gui.Borrow_book(info_book), ["0", "00"])


## Personal_information
def Personal_info(info_personal:dict):
    return show_fix(gui.Personal_info(info_personal), ["1","2","3","0"])

def Edit_info_member(info_personal:dict):
    return show_content('Edit personal information', info_personal, type_syntax="")

def Object_edit_info_member(object:str):
    os.system('clear')
    print(gui.Object_edit_info_member(object))
    object_edit_info_member = input(f"Enter: ")
    return object_edit_info_member

def Done_edit_info_member(object:str):
    return show_fix(gui.Done_edit_info_member(object),["0","00"])

############### admin ##################
def Main_admin():
    return show_fix(gui.Main_admin(), ["1","2","3"])

def Manage_member():
    return show_fix(gui.Manage_member(), ["1","2","0"])

def Overview_member(guests, students, teachers):
    return show_fix(gui.Overview_member(guests, students, teachers), ["0", "00"])

def Detail_member(member_list:list):
    return show_content("Detail Member", member_list)

def Choose_member(info_member:dict):
    return show_fix(gui.Choose_member(info_member), ["1","2","3","0","00"])

def Books_of_member(username, list_book):
    return show_fix(gui.Books_of_member(username, list_book), ["0","00"])

def Remove_member(info_member:dict):
    return show_fix(gui.Remove_member(info_member), ["0","00"])

def Manage_book():
    return show_fix(gui.Manage_book(), ["1","2","3","0"])

def Overview_book(numbers):
    return show_fix(gui.Overview_book(numbers), ["0", "00"])

def Detail_book(book_list:list):
    return show_content("Detail Book", book_list)

def Edit_info_book(info_book:dict):
    return show_content('Edit book information', info_book, type_syntax="")

def Object_edit_info_book(object:str):
    os.system('clear')
    print(gui.Object_edit_info_book(object))
    object_edit_info_book = input(f"Enter: ")
    return object_edit_info_book

def Done_edit_info_book(object:str):
    return show_fix(gui.Done_edit_info_book(object),["0","00"])

def Choose_book_admin(info_book:dict):
    return show_fix(gui.Choose_book_admin(info_book), ["1","2","0","00"])

def Remove_book(info_book:dict):
    return show_fix(gui.Read_book(info_book), ["0","00"])

def Add_book():
    os.system('clear')
    print(gui.Add_book())
    title = input("Title of book: ")
    author = input("Author of book: ")
    subject = input("Subject of book: ")
    link = input("PDf_link of book: ")
    book = {'title':title, 'author':author, "subject":subject, "PDF_link":link} # creat new book
    return book

def Done_add_book(info_book:dict):
    return show_fix(gui.Done_add_book(info_book), ["0","00"])





# member_list = ["a", "b"]
# info_book = {'title': 1, "name":2}


# Done_add_book(info_book)
