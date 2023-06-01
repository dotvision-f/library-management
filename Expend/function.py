# SEARCH
# Search by title
def search_by_title():
    pass

# Search by authors
def search_by_authors():
    pass

# Search by subject
def search_by_subject():
    pass

########################################

# Log In / Sign Up / Log Out / Reset Password
# Log in
def log_in():
    pass

# Sign up
# Yeu cau: gui xac nhan vao email de xac nhan roi moi nhap duoc password dang ky
def sign_up():
    pass

# Log Out
def log_out():
    pass

# Reset Password
## Yeu cau: tuong tu Sign Up
def reset_password():
    pass

class Address:
    def __init__(self,province, district, ward, street = ""):
        self.province = province
        self.district = district
        self.ward = ward
        self.streeet = street
    
    def __call__(self):
        return f"{self.province}, {self.district}, {self.ward}, {self.streeet}"
