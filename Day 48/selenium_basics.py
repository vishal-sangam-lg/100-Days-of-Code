from selenium import webdriver

# chrome_driver is downloaded from https://chromedriver.chromium.org/downloads
chrome_driver_path = "/Users/vishalsangamlg/AI ML DS/100-Days-of-Code/chromedriver_mac_arm64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")

# driver.close()
driver.quit()
