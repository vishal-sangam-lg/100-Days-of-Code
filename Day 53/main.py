from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B"
                        "%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west"
                        "%22%3A-122.56413546923828%2C%22east%22%3A-122.30252353076172%2C%22south%22%3A37"
                        ".67604010319295%2C%22north%22%3A37.87441073873394%7D%2C%22regionSelection%22%3A%5B%7B"
                        "%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C"
                        "%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22"
                        "%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D"
                        "%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22"
                        "%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22"
                        "%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A616647%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C"
                        "%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".property-card-link")

all_links = []
for link in all_link_elements:
    href = link["href"]
    # print(href)
    if "http" not in href:
        if f"https://www.zillow.com{href}" not in all_links:
            all_links.append(f"https://www.zillow.com{href}")
    else:
        if href not in all_links:
            all_links.append(href)
print("links: ", all_links, len(all_links))

all_address_elements = soup.select(".property-card-link address")
all_addresses = [''.join(address.get_text().split(" | ")) for address in all_address_elements]
print("addresses: ", all_addresses, len(all_addresses))

all_price_elements = soup.select(".property-card-data div span")
all_prices = [price.get_text().split("+")[0] for price in all_price_elements if "$" in price.text]
print("prices: ", all_prices, len(all_prices))

chrome_driver_path = "/Users/vishalsangamlg/AI ML DS/100-Days-of-Code/chromedriver_mac_arm64/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

for i in range(len(all_links)):
    # Opening google form
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdqiTtPmAJiKrfBD5i_B1D90qWvjDXFfdPZOvqf6gTq_qEF0w/viewform?usp=sf_link")

    time.sleep(3)
    address = driver.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div['
                                  '1]/input')
    price = driver.find_element(By.XPATH,
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_addresses[i])
    price.send_keys(all_prices[i])
    link.send_keys(all_links[i])
    submit_button.click()
