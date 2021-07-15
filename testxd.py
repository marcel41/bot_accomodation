from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import credentials

from selenium.webdriver import ActionChains
# url = 'https://accommodation.fmel.ch/StarRezPortal/AE18865B/7/8/Login-Login?IsContact=False'
USERNAME = credentials.USERNAME
PASSWORD = credentials.PASSWORD

driver = webdriver.Chrome('./chromedriver')
# driver.get("https://www.python.org")
# # driver.get('http:/reddit.com')
# window_before = driver.window_handles[0]
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
# window_after = driver.window_handles[1]
# driver.switch_to_window(window_after)
# time.sleep(3)
# driver.get('http://bing.com')


urls = ["https://accommodation.fmel.ch/StarRezPortal/AE18865B/7/8/Login-Login?IsContact=False"]
        # "https://business.google.com/u/0/edit/l/13532588171385373346?hl=fr",
        # "https://business.google.com/edit/l/18307083220547614220",
        # "https://business.google.com/u/0/edit/l/08603059593698723407?hl=fr",
        # "https://business.google.com/edit/l/00810825496818981035"]
booking_link = "https://accommodation.fmel.ch/StarRezPortal/2E58607A/71/1105/Book_now-Continue_to_Booking"
element = "<button>Login</button>"

action_chains = ActionChains(driver)

for posts in range(len(urls)):
    print(posts)
    driver.get(urls[posts])
    time.sleep(5)
    if posts == 0:
        #loggin to website
        print("HELLO")
        driver.find_element_by_name("Password").send_keys(PASSWORD)
        driver.find_element_by_name("Username").send_keys(USERNAME)

        # ActionChains(driver).click(element).perform()
        driver.find_element_by_css_selector('[class="ui-btn-login sr_button_primary sr_button"]').click()
        time.sleep(5)
        # driver.get(booking_link)
        driver.find_element_by_css_selector('[class="ui-nav-process nav-item"]').click()
        driver.find_element_by_css_selector('[class="ui-submit-page-content sr_button_primary sr_button"]').click()
        # driver.find_element_by_css_selector('.btn.btn-primary').click()

        page = driver.find_element_by_tag_name('body')

        page.send_keys(Keys.CONTROL + 't')



    if(posts!=len(urls)-1):
       driver.execute_script("window.open('');")
       chwd = driver.window_handles
       driver.switch_to.window(chwd[-1])

chwd = driver.window_handles
print(chwd)
