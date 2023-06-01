
class gui:
    def Title(title):
        return f'''
-------------------------------------------
        {title}
-------------------------------------------'''


    home = '''
-------------------------------------------
   Welcome to the Digital Library   
-------------------------------------------
1. Log in / Sign up
2. Exit
'''
#Enter the number:

    username = '''
-------------------------------------------
              Log in / Sign up
-------------------------------------------'''
# Username or Email:
# Enter password or Forget password (4P - Forget/enter Password)
    def Password_4P(email):
        return f'''
-------------------------------------------
                Log in
-------------------------------------------
Welcome {email} back to the library.
Please enter a password.

(If you forgot your password, enter the number "1" to retrieve your password)
'''
# Enter the password:

    # Forget password
    def Forget_password(email):
        return f'''
-------------------------------------------
               Forget password
-------------------------------------------
Your request to forget your password has been sent via email {email},
Please check your email and follow the instructions.

Enter the number "0" to back to home page.
'''
# Enter the number:

    # Sign Up
    def Password_1(email):
        return f'''
-------------------------------------------
                Sign up
-------------------------------------------
Welcome {email} to the library.
Let's create a new password
'''
# Enter the password:

    # Done Sign Up
    done_sign_up = '''
-------------------------------------------
                Sign Up
-------------------------------------------
You have successfully registered.

Enter the number "0" to login
'''
# Enter the number:



####################### Màn hình trang chủ sau đăng nhập ################################
    # Main_SignIn_Success
    def Main(username):
        return f"""
-------------------------------------------
            The Digital Library 
-------------------------------------------
Welcome {username} to the library.

1. Read / Borrow book
2. Personal information
3. Log out
"""
# Enter the number:

    ## Read / Borrow books 
    read_borrow_book = """
-------------------------------------------
            Read / Borrow books 
-------------------------------------------
Read / Borrow books 

1. Your book list
2. Search by title
3. Search by Author
4. Search by Subject
0. Back to Home Page
"""
# Enter the number:

    ### Your book list
    your_book_list = """
-------------------------------------------
            Your book list
-------------------------------------------
Your book list

1. Your online book list
2. Your offline book list
0. Back to Home Page
00. Back to Previous Page
"""
# Enter the number:

    #### Your online book list
#     your_online_book_list = """
# -------------------------------------------
#             Your online book list
# -------------------------------------------
# #### Noi dung gioi thieu . NHAP TAI DAY###
# Danh sách các cuốn sách online của bạn
# ...

# Enter the number of the book OR
# 0. Back to Home Page
# 00. Back to Previous Page

# Enter the number: """

    ##### Choose book (online)
    def Online_choose_book(info_book:dict):
        strs = f"""
-------------------------------------------
        Book: "{info_book['title']}"
-------------------------------------------
"""
        for i in info_book:
            strs += f"{i}: {info_book[i]}\n"
        strs+="""
1. Đọc sách
2. Download pdf file (Only teacher)
3. Remove from list
0. trở về home page
00. trở về trang trước
"""
        return strs

# Enter the number:


    ###### Read book
    def Read_book(info_book:dict):
        return f"""
-------------------------------------------
        Reading "{info_book['title']}"
-------------------------------------------
Bạn đang đọc cuốn sách "{info_book['title']}" tại một cửa sổ mới.

0. trở về home page
00. trở về trang trước
"""
# Enter the number:

    ###### Download pdf file
    def Download_pdf_file(info_book:dict):
        return f"""
-------------------------------------------
  Download pdf file of "{info_book['title']}"
-------------------------------------------
Xin thông cảm, tính năng đang được nâng cấp"".

0. trở về home page
00. trở về trang trước
"""
# Enter the number:

    ###### Remove from list
    def Remove_from_list(info_book:dict):
        return f"""
-------------------------------------------
  Remove "{info_book['title']}"
-------------------------------------------
Bạn đã xoá cuốn "{info_book['title']}" khỏi danh sách sách của bạn.

0. trở về home page
"""
# Enter the number:

    #### Your offline book list
#     your_offline_book_list = """    
# -------------------------------------------
#             Your offline book list
# -------------------------------------------
# Danh sách các cuốn sách mượn tại thư viện của bạn
# ...

# Enter the number of the book OR
# 0. Back to Home Page
# 00. Back to Previous Page

# Enter the number: """

    ##### Choose book (title)
    def Office_choose_book(info_book:dict):
        strs = f"""
-------------------------------------------
        Book: "{info_book['title']}"
-------------------------------------------
"""
        for i in info_book:
            strs += f"{i}: {info_book[i]}\n"
        strs+="""
1. Return book
0. trở về home page
00. trở về trang trước
"""
        return strs

    ###### Return book
    def Return_book(info_book:dict):
        return f"""
-------------------------------------------
    Return book {info_book['title']}
-------------------------------------------
Bạn đã đăng ký trả sách thành công, vui lòng mang sách đến thư viện trong
vòng 24h kể từ khi đăng ký thành công.

0. trở về home page
00. trở về trang trước
"""
# Enter the number:

    ### Search by ...
    def Type_of_search(name_type:str):
        return f"""
-------------------------------------------
            Search by {name_type}
-------------------------------------------
Enter the {name_type} of book OR

0. trở về home page
00. trở về trang trước
"""
# Enter the title:

    #### list_search (title)
#     def Title_list_search(list_search:list):
#         strs ="""
# -------------------------------------------
#             Search by title
# -------------------------------------------
# """
#         for i in list_search:
#             strs += f"{i}: {list_search[i]}\n"
#         strs+="""
# 1. Return book
# 0. trở về home page
# 00. trở về trang trước
# """

    ##### Choose book (title, author, subject)
    def Choose_book(info_book:dict):
        strs = f"""
-------------------------------------------
        Book: "{info_book['title']}"
-------------------------------------------
"""
        for i in info_book:
            strs += f"{i}: {info_book[i]}\n"
        strs+="""
1. Read book
2. Borrow book
3. Download pdf file
0. trở về home page
00. trở về trang trước
"""
        return strs

    #### Return book
    def Borrow_book(info_book:dict):
        return f"""
-------------------------------------------
    Borrow book "{info_book['title']}
-------------------------------------------
Bạn đã đăng ký mượn sách thành công, vui lòng đến thư viện trong
vòng 24h để lấy sách kể từ khi đăng ký thành công.

0. trở về home page
00. trở về trang trước
"""
# Enter the number:



    ## Personal information
    def Personal_info(info_personal:dict):
        strs = """
-------------------------------------------
            Personal information
-------------------------------------------
"""
        for i in info_personal:
            strs += f"{i}: {info_personal[i]}\n"
        strs+="""
1. Your online book list
2. Your offline book list
3. Chinh sua thong tin ca nhan
0. Back to Home Page
"""
        return strs
# Enter the number:

###
#     def Edit_info_member(info_personal:dict):
#         strs = """
# -------------------------------------------
#             Edit personal information
# -------------------------------------------
# """
#         for i in info_personal:
#             strs += f"{i}: {info_personal[i]}\n"
#         strs+="""
# Enter the object to edit OR

# 0. Back to Home Page
# 00. Back to Previous Page
# """
        # return strs
# Enter the object:

####
    def Object_edit_info_member(object:str):
        return f"""
-------------------------------------------
        Edit personal information
-------------------------------------------
Type the new {object} OR

0. Back to Home Page
00. Back to Previous Page
"""
# Enter:

#####
    def Done_edit_info_member(object:str):
        return f"""
-------------------------------------------
        Edit personal information
-------------------------------------------
You have done to edit {object}.

0. Back to Home Page
00. Back to Previous Page
"""
# Enter the number:



###################### Admin ######################
    def Main_admin():
        return f"""
-------------------------------------------
        Admin - The Digital Library 
-------------------------------------------

1. Manage member
2. Manage book
3. Log out
"""
# Enter the number:
    ##
    def Manage_member():
        return f"""
-------------------------------------------
                Manage Member
-------------------------------------------

1. Overview member
2. Detail member
0. Back to Home Page
"""
# Enter the number:
    ###
    def Overview_member(guests, students, teachers):
        return f"""
-------------------------------------------
            Overview Member
-------------------------------------------
The number of members: {guests + students + teachers}
Include:
        Guests: {guests}
        Students: {students}
        Teachers: {teachers}

0. Back to Home Page
00. Back to Previous Page
"""
# Enter the number:
    ###
#     def Detail_member(member_list): # same Your offline book list
#         return f"""
# -------------------------------------------
#             Detail Member
# -------------------------------------------
# ### Show list of member

# Type the number of member OR

# 0. Back to Home Page
# 00. Back to Previous Page
# """
# Enter the number:
    ####
    def Choose_member(info_member:dict):
        strs = f"""
-------------------------------------------
            Member {info_member['email']}
-------------------------------------------
"""
        for i in info_member:
            strs += f"{i}: {info_member[i]}\n"
        strs+="""
        
1. Edit information
2. Books of member
3. Remove member
0. Back to Home Page
00. Back to Previous Page
"""
        return strs
# Enter the number:
    #####
    def Books_of_member(username, list_book:list):
        strs = f"""
-------------------------------------------
        Books of "{username}"
-------------------------------------------
"""
        for i in range(len(list_book)):
            strs += f"Number {i+1}: {list_book[i]}\n"
        strs+="""
0. Back to Home Page
00. Back to Previous Page
"""
        return strs
# Enter the number:

    def Remove_member(info_member:dict):
        strs = f"""
-------------------------------------------
            Remove {info_member['email']}
-------------------------------------------
Ban da remove member {info_member['name']} thanh cong.

0. Back to Home Page
00. Back to Previous Page
"""
        return strs
# Enter the number:

    ##
    def Manage_book():
        return f"""
-------------------------------------------
                Manage Book
-------------------------------------------

1. Overview book
2. Detail book
3. Add book
0. Back to Home Page
"""
    ###
    def Overview_book(numbers):
        return f"""
-------------------------------------------
            Overview Book
-------------------------------------------
Number of books: {numbers}

0. Back to Home Page
00. Back to Previous Page
"""
# Enter the number:



    ###
#     def Detail_book(member_list): # same Your offline book list
#         return f"""
# -------------------------------------------
#             Detail Book
# -------------------------------------------
# ### Show list of book

# Type the number of book OR

# 0. Back to Home Page
# 00. Back to Previous Page
# """
# Enter the number:
    ####
    def Choose_book_admin(info_book:dict):
        strs = f"""
-------------------------------------------
        Book: "{info_book['title']}"
-------------------------------------------
"""
        for i in info_book:
            strs += f"{i}: {info_book[i]}\n"
        strs+="""
1. Edit information
2. Remove book
0. Back to Home Page
00. Back to Previous Page
"""
        return strs
# Enter the number:


    def Object_edit_info_book(object:str):
        return f"""
-------------------------------------------
            Edit book information
-------------------------------------------
Type the new {object} OR

0. Back to Home Page
00. Back to Previous Page
"""
# Enter:

#####
    def Done_edit_info_book(object:str):
        return f"""
-------------------------------------------
        Edit book information
-------------------------------------------
You have done to edit {object}.

0. Back to Home Page
00. Back to Previous Page
"""
# Enter the number:


    #####
    def Remove_book(info_book:dict):
        return f"""
-------------------------------------------
        Remove {info_book['title']}
-------------------------------------------
Ban da ramove book "{info_book['title']}" khoi thu vien

0. Back to Home Page
00. Back to Previous Page
"""
# Enter the number:
    ###
    def Add_book():
        return f"""
-------------------------------------------
                Add book
-------------------------------------------
"""
# Name of book
# Author of book
# Subject of book
# Type of book

    def Done_add_book(info_book:dict):
        return f"""
-------------------------------------------
        Add book {info_book['title']}
-------------------------------------------
Done

0. Back to Home Page
00. Back to Previous Page
"""