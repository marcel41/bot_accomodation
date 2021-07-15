import credentials
from autologin import AutoLogin

# url = 'https://accommodation.fmel.ch/StarRezPortal/AE18865B/7/8/Login-Login?IsContact=False'
url = 'https://accommodation.fmel.ch/StarRezPortal/AE18865B/7/8/Login-Login?IsContact=False'
USERNAME = credentials.USERNAME
PASSWORD = credentials.PASSWORD

def connect():
    pass

if __name__ == "__main__":
    al = AutoLogin()
    cookies = al.auth_cookies_from_url(url, USERNAME, PASSWORD)
    pass
