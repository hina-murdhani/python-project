import random

import xlsxwriter

workbook = xlsxwriter.Workbook('data_1700.xlsx')
worksheet = workbook.add_worksheet()
name = open("C:/Users/hina.murdhani/Downloads/dummy_resume_creator/dummy_resume_creator/name_file.txt",
            "r").read().lower()
name = set(name.split())
email = []
username = []
usercontact = []

row = 0
column = 0

for i in range(1000):
    email_name = list(name)[random.randint(0, len(name)) - 1]
    email_id = email_name + "70" + str(random.randint(1111, 9999)) + "@20minutemail.it"
    email.append(email_id)
    username.append(email_name)
    number = str(random.randint(1111111111, 9999999999))
    contact = "+91" + number
    usercontact.append(contact)

row = 0
for i in username:
    worksheet.write(row, column, i)
    row += 1

row = 0
for i in email:
    worksheet.write(row, column+1, i)
    row += 1

row = 0
column = 0
for i in usercontact:
    worksheet.write(row, column + 2, i)
    row += 1

workbook.close()
