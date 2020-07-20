import smtplib
import os
from email.message import EmailMessage

email_address= 'youremail@email.com'
email_password = 'yourpassword'

message = EmailMessage()
message['from'] = email_address
message['to'] = 'senderemailaddres@email.com'
message['subject'] = 'Content Subject'

#body
with open('index.html','r') as my_html:
  html_content = my_html.read()
message.set_content(html_content,'html')

#adding attachments to email(image)
image_name = 'akshajdev2.jpg'
with open(image_name,'rb') as f:
  image = f.read()
  file_name,file_type = os.path.splitext(image_name)[0],os.path.splitext(image_name)[1]

message.add_attachment(image,maintype = 'image',subtype= file_type,filename = file_name)


with smtplib.SMTP('smtp.gmail.com',587) as smtp:
   smtp.ehlo()
   smtp.starttls()
   smtp.login(email_address,email_password)
   smtp.send_message(message)
   smtp.quit()

