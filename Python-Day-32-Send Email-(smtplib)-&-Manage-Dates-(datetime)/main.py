import smtplib
import datetime as dt
import random

my_email = "gogulanravismtp@gmail.com"
password = "" ##Enter password


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Thursday Motivation\n\n{quote}"
        )




# import smtplib
#
# my_email = "gogulanravismtp@gmail.com"
# password = "" ##Enter password
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="gogulanravismtp@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
# # don't need connection.close()

# ####datetime#####
# import datetime as dt
#
#
# now = dt.datetime.now()
# year = now.year
# # if year == 2022:
# #     print("Wear a face mask")
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)


