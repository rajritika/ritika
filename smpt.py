import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('ritikargar99@gmail.com', 'akitir99') #login to the server
msg = 'Hello!' #send the mail
server.sendmail('ritikargar99@gmail.com', 'sahanagowda257@gmail.com', msg) # The /n separates the message from the headers
server.close()
