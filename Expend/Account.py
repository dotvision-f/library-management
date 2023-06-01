# Thong tin chung ve tai khoan
from Expend.function import *
from Expend.constant import *
from datetime import datetime, date
from abc import ABC
## id, password, status

class Account(ABC):
    def __init__(self, email, password, level):
        self.email = email
        self.__password = password
        self.level = level
    
    def get_password(self):
        return self.__password
    
    def change_password(self, password):
        self.__password = password
      

# Tai khoan cua nguoi ben ngoai truong.
'''
- Log In / Sign Up / Log Out / Reset Password (function)
- Search Book: by Title, Author, Subject (function)
- Read free Book
- View/ Change Profile: Profile, Store
'''
class Guest(Account):
    def __init__(self, email, password, level=None):
        super().__init__(email, password, level)
    
    # Log In / Sign Up / Log Out / Reset Password
    ### ĐƯỢC LẬP TRÌNH LOGIC TRONG GIAO DIỆN
    def log_in(self):
        return log_in()
    def sign_up(self):
        return sign_up()
    def log_out(self):
        return log_out()
    def reset_password(self):
        return reset_password()
    
    # SEARCH
    ### ĐƯỢC LẬP TRÌNH LOGIC TRONG GIAO DIỆN
    def search_by_title(self):
        return search_by_title()
    def search_by_author(self):
        return search_by_authors()
    def search_by_subject(self):
        return search_by_subject()
    
    # Read book: Doc mot so cuon sach Free.
    def read_book(self): #####
        pass

    # View/ Change Profile: Profile, Store
    def info(self):#####
        pass
    
    # show Store. Thong tin cac cuon sach pdf va sach giay muon tu thu vien
    def info_store(self):#####
        pass

    # edit account. Parameters: id/name/... , nội dung edit + Edit in database
    def edit_info(self, parameter, edit):
        pass


# Tai khoan danh cho sinh vien
'''
- Register: Borrow / Return Book
- Read full Book
'''
class Student(Guest):
  def __init__(self, email, password, level):
    super().__init__(email, password, level)
    self.archives = {}

  def get_info(self):
     ###### Return 1 dict cac thong so
     pass
  
  # def borrow_book(self, book: Book):
  #   if self.type not in ["student", "teacher"]:
  #     return print('Bạn không đủ level mượn sách')    
  #   elif self.status == "block":
  #     print(f"Tài khoản {self.email} của bạn đã bị chặn quyền mượn sách.")
  #   elif self.status == "cancel":
  #     print("Tài khoản của bạn đã bị xóa.")
  #   elif len(self.archives) >= 5:
  #       print("Bạn đã mượn tối đa số lượng sách có thể mượn.")
  #   elif book.number_of_book <= 0:
  #     print("Sách đã hết, vui lòng chọn sách khác.")
  #   else:
  #     print("Bạn có thể đọc quyển sách này bây giờ.")
  #     choice = input("Bạn muốn mượn quyển sách này chứ ? (y/n) ")
  #     if choice.lower() == "y" and book not in self.archives:
  #         ngay_muon = date.today()
  #         self.archives[book] = ngay_muon
  #         book.number_of_book -= 1
  #         print("Đã thêm sách thành công, bạn có thể đến thư viện mượn sách")
  #     else:
  #       print(f"Tài khoản {self.email} đã hủy thao tác")
    
  # def return_book(self, book: Book):
  #   if self.type not in ["student", "teacher"]:
  #     print("Bạn không thể thực hiện chức năng này")
  #   elif book not in self.archives:
  #     print("Không tìm thấy thông tin sách muốn trả")
  #   else:
  #     ngay_tra = date.today()
  #     thoi_diem_tra = datetime.combine(ngay_tra, datetime.time.min)
  #     ngay_muon = self.archives[book]
  #     tinh_trang = "đúng hạn" if thoi_diem_tra <= ngay_muon + timedelta(days=30) else "quá hạn"
  #     print(f"Bạn đã trả sách {tinh_trang}")
  #     del self.archives[book]
  #     book.number_of_book += 1


# Tai khoan danh cho giao vien
'''
- Download pdf file
'''
class Teacher(Student):
  def __init__(self, email, password, level):
    super().__init__(email, password, level)

  def dowload_pdf(self):
      print("Bạn có thể tải file PDF")

# Tai khoan cua admin
'''
- Edit/ Add/ Remove Book
- Edit/ Block/ Unblock/ Remove Member
'''
class Admin(Teacher):
    def __init__(self, email, password, level):
        super().__init__(email, password, level)

    ## BOOK
    # add Book. + Add to database
    def add_book(self, Book):
        ##### Them sach vao database
        pass

    # remove Book + Delete in database
    def remove_book(self, Book):
        ##### Xoa sach khoi Database
        pass

    # sua noi dung sach. Parameters: id/name/... , nội dung edit + Edit in database
    def edit_book(self, Book, feature, edit):
        pass
    
    ## MEMBER
    # edit member. Parameters: id/name/... , nội dung edit + Edit in database
    def edit_member(self, Member, features, edit):
        ##### Edit info
        pass

    # remove member + Delete in database
    def remove_member(self, Member):
        ##### Xoa thanh vien khoi Database
        pass


# Luu tru thong tin cua cac Account Member
## name, address, email, number phone
class Person:
    pass
