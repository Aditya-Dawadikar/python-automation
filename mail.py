import smtplib

content ="first email"
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()

mail.starttls()
mail.login('adityadawadikar2000', 'adipraneet')
mail.sendmail('adityadawadikar2000','adityadawadikar2000',content)
mail.close()