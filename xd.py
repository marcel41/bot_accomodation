from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import credentials
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
# from selenium import Options
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.action_chains import ActionChains
# url = 'https://accommodation.fmel.ch/StarRezPortal/AE18865B/7/8/Login-Login?IsContact=False'
USERNAME = credentials.USERNAME
PASSWORD = credentials.PASSWORD

# chromedriver  = "./chromedriver"
driver = webdriver.Chrome('./chromedriver')

# chrome_options = Options()
# chrome_options.add_extension('Path\to\the\crx\file')
# driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)

driver.get("https://www.python.org")
e = driver.find_element_by_xpath("//*[text()='Donate']");
location = e.location
size = e.size
w, h = size['width'], size['height']

print(location)
print(location['x'])
print(location['y'])
print(size)
print(w, h)

# ActionChains(driver).move_by_offset(e.location['x'], e.location['y']).click().perform() # Left mouse click, 200 is the x coordinate, 100 is the y coordinate

actionChains = ActionChains(driver)
# actionChains.move_to_element(e).click().perform()

e = driver.find_element_by_xpath("//*[text()='Downloads']");
time.sleep(5)
e.click()
# actionChains.move_to_element(e).perform()
# driver.execute_script("arguments[0].scrollIntoView();", e)

# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
