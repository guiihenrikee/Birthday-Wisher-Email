import smtplib
import random
import pandas
import os
from datetime import datetime
"""YOU NEED TO DEACTIVATE THE "LESS SECURE APP ACCESS" AND DISABLE 2-STEP VERIFICATIONS
 ON YOUR GMAIL SECURITY SETTINGS FOR THE CODE WORKS """
YOUR_NAME = "YOUR NAME" #-#-#-#-#-#-#-
MY_EMAIL = "YOUR EMAIL" #-#-#-#-#-#-#-
PASSWORD = "YOUR EMAIL PASSWORD" #-#-#-#-#-#-

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    letter_choice = random.choice(os.listdir("./letter_templates"))
    with open(f"./letter_templates/{letter_choice}") as letter_to_send:
        letter = letter_to_send.read()
        letter = letter.replace("[NAME]", birthday_person["name"])
        letter = letter.replace("[SENDER NAME]", YOUR_NAME)  #-#-#-#-#-#-#-#-

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    """IF YOUR EMAIL ISN`T GMAIL, YOU NEED A DIFFERENT SMTP AND PORT ADRESS. """
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=birthday_person["email"],
                        msg=f"Subject: Happy Birthday!\n\n{letter}")
    connection.close()

