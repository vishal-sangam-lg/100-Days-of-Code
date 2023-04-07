import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "aditirao292@gmail.com"
MY_PASSWORD = "CD9A4DEA1D457B9C39EDA1CC8F2271F24C18"

url = "https://www.amazon.in/dp/B0BDJ6ZMCC?th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_="a-price-whole").get_text()
stripped_price = price[:-1]
formatted_price = stripped_price.replace(",", "")
price_as_float = float(formatted_price)
print(price_as_float)
price_that_you_want_to_buy = 120000

if price_as_float < price_that_you_want_to_buy:
    print("Sending Email...")
    with smtplib.SMTP("smtp.elasticemail.com", 2525) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="lgvishalsangam@gmail.com",
            msg=f"Subject:Current Price of iPhone 14 Pro is Rs. {stripped_price}."
        )
    print("Email sent successfully!")
else:
    print("Price is greater than your expectations.")
