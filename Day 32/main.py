# import smtplib
#
# my_email = "aditirao292@gmail.com"
# password = "APP_PASSWORD"
#
# # Syntax (old)
# # connection = smtplib.SMTP("smtp.elasticemail.com")
# # connection.starttls()
# # connection.login(user=my_email, password=password)
# # connection.sendmail(from_addr=my_email, to_addrs="lgvishalsangam@gmail.com", msg="Hello")
# # connection.close()
#
# # Better syntax
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="lgvishalsangam@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# import datetime as dt
#
# now = dt.datetime.now()
#
# print(now)
# print(now.year)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)
#
