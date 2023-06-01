class User:
    def __init__(self, username, password, new_password):
        self.username = username
        self.password = password
        self.new_password = new_password

class Library:
    def __init__(self):
        self.users = []
        self.logged_in_user = None

    def register_user(self, username, password):
        # Kiểm tra xem người dùng đã tồn tại hay chưa
        for user in self.users:
            if user.username == username:
                print("Tài khoản đã tồn tại!")
                return

        # Đăng kí một người dùng mới
        new_user = User(username, password)
        self.users.append(new_user)
        print("Đăng kí thành công!")

    def login(self, username, password):
        # Đăng nhập người dùng
        for user in self.users:
            if user.username == username and user.password == password:
                self.logged_in_user = user
                print("Đăng nhập thành công")
                return
        print("Sai mật khẩu hoặc tài khoản")

    def logout(self):
        # Đăng xuất người dùng
        self.logged_in_user = None
        print("Hẹn gặp lại!")

    def change_password(self, current_password, new_password):
        # Thay đổi mật khẩu người dùng đang đăng nhập
        if self.logged_in_user:
            if self.logged_in_user.password == current_password:
                if self.logged_in_user.password == new_password:
                    print("Mật khẩu mới trùng với mật khẩu hiện tại")
                else:
                    self.logged_in_user.password = new_password
                    print("Thay đổi mật khẩu thành công!")
            else:
                print("Nhập sai mật khẩu hiện tại")
        else:
            print("Bạn phải đăng nhập để đổi mật khẩu")
