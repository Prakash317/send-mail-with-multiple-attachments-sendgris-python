import sendgrid
from sendgrid.helpers.mail import *
import base64, os

send_grid_api_key = sendgrid.SendGridAPIClient(api_key="your_sendgrid_api_key")

class EmailSender:
	def build_attachments(self, filepath)
	attachments = []
	for file in filepath:
		name = os.path.basename(file)
		type = name.split('.')
		with open(file, 'rb')as f:
			data = f.read()
			f.close()
		encoded = base64.b64encode(data).decode()
		attcahment = Attachment()
		attachment.file_content = FileContent(encoded)
		attachment.file_type = FileType(type[1])
		attachment.file_name = FileName(name)
		attachments.append(attachment)	
	return attachments

	def send_mail(self, sender, to, subject, body, attachments=None):
	content = PlainTextContent(body)
	message = Mail(from_email=sender,
            		to_emails=to,
            		subject=sub,
            		html_content=content)
            if attachments:
            	for attachment in attachments:
            		message.add_attachment(attachment)
  try:
	  response = sg.send(message)
  except Exception as error:
    print(error)
	return response.status_code
	
def test_mail():
	sender = "sender_email_id"
	to = ["emil_id1", "email_id2"]
	sub = "Your subject"
	body = "Type your body here,\n Regards,\n Prakash317"
  attachmentFilePath = ["home/tl023/file.txt","home//tl023/file2.pdf"]
  email_sender = EmailSender()
  attach = email_sender.build_attachment(attachmentFilePath)
  response = email_sender.send_mail(sender, to, sub, body, attach)
  print(response.status_code)
    	
test_mail()

    	
    	
