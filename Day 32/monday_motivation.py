# Automated Monday Motivation emailer
import smtplib
import datetime as dt
import random

MY_EMAIL = "aditirao292@gmail.com"
MY_PASSWORD = "CD9A4DEA1D457B9C39EDA1CC8F2271F24C18"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.elasticemail.com", 2525) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Monday Motivation\n\n{quote}")
