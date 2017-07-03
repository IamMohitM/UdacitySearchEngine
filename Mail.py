import smtplib

try:
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("mohit@axelta.com","Axelta@1")
    server.sendmail("mohit@axelta.com","vinu849@gmail.com","Hello ")
    server.quit()
except Exception,Argument:
    print "There you go: ",Argument


