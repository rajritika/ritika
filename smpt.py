import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('ritikargar99@gmail.com', 'akitir99')
msg = 'Hello!'
server.sendmail('ritikargar99@gmail.com', 'sahanagowda257@gmail.com', msg)
server.close()
