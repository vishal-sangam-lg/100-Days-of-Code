from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# chrome_driver is downloaded from https://chromedriver.chromium.org/downloads
chrome_driver_path = "/Users/vishalsangamlg/AI ML DS/100-Days-of-Code/chromedriver_mac_arm64/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)


# driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# docs_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(docs_link.text)

# donate_link = driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[1]/a')
# print(donate_link.text)

# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# events = {}
#
# for i in range(len(event_times)):
#     events[i] = {
#         "time": event_times[i].text,
#         "name": event_names[i].text
#     }
# print(events)


# -----------------Interactions------------------- #
# Clicking, Typing input and Searching, Filling out forms

driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
# article_count.click()

# Wikibooks = driver.find_element(By.LINK_TEXT, "Wikibooks")
# Wikibooks.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


time.sleep(5)
# driver.close()
driver.quit()
