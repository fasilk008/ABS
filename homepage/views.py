from django.shortcuts import render, render_to_response
from django.template import RequestContext
from unidecode import unidecode
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import HttpResponse
import smtplib
from email.mime.text import MIMEText

from homepage.models import Pages,Items,Photo
# Create your views here.
def homeview(request):
	home_data = Pages.objects.all().order_by('id')
	for data in home_data:
		if data.type=='Home':
			home_header = unidecode(data.header)
			home_desc = unidecode(data.desc)
		elif data.type == 'Service':
			service_header = unidecode(data.header)
			service_desc = unidecode(data.desc)
		elif data.type == 'About':
			about_header = unidecode(data.header)
			about_desc = unidecode(data.desc)
		elif data.type == 'Faq':
			faq_header = unidecode(data.header)
			faq_desc = unidecode(data.desc)
	home_items = Items.objects.filter(page=Pages.objects.get(type="Home")).order_by('id')
	if len(home_items) > 0:
		homedata1_header = unidecode(home_items[0].header)
		homedata1_text = unidecode(home_items[0].text)
		homedata1_image = str(home_items[0].image)
	if len(home_items) > 1:
		homedata2_header = unidecode(home_items[1].header)
		homedata2_text = unidecode(home_items[1].text)
		homedata2_image = str(home_items[1].image)
	if len(home_items) > 2:
		homedata3_header = unidecode(home_items[2].header)
		homedata3_text = unidecode(home_items[2].text)
		homedata3_image = str(home_items[2].image)
	if len(home_items) > 3:
		homedata4_header = unidecode(home_items[3].header)
		homedata4_text = unidecode(home_items[3].text)
		homedata4_image = str(home_items[3].image)
	service_items = Items.objects.filter(page=Pages.objects.get(type="Service")).order_by('id')
	about_item = Items.objects.get(page=Pages.objects.get(type="About"))
	faq_items = Items.objects.filter(page=Pages.objects.get(type="Faq")).order_by('id')
	return render_to_response('home.html', locals(), RequestContext(request))


@csrf_exempt
def email_compose(request):
	if request.method=='POST':
		print request.POST
		name = request.POST.get("name",'')
		print name
		email = request.POST.get('email',None)
		print email
		phone = request.POST.get('phone',None)
		print phone
		message = request.POST.get('message',None)
		print message
		email_subject = "Website Contact Form:  " + name
		email_body = "You have received a new message from your website contact form.\n\n"
		email_body = email_body + "Here are the details:\n\nName: " + name + "\n\nEmail: " + email 
		email_body = email_body + "\n\nPhone: " + phone + "\n\nMessage:" + message
		SMTP_SERVER = "p3plcpnl0613.prod.phx3.secureserver.net"
		SMTP_PORT = 587
		SMTP_USERNAME = 'noreply@annualbusinessservices.us'
		SMTP_PASSWORD = 'pass123#1'
		email_from = 'noreply@annualbusinessservices.us'
		email_to = ['support@annualbusinessservices.us']
		email_message = MIMEText(email_body)
		email_message['Subject'] = email_subject
		email_message['From'] = email_from
		email_message['To'] = ', '.join(email_to)
		smtp = smtplib.SMTP(
			host = SMTP_SERVER,
			port = SMTP_PORT,
			timeout = 10
		)
		smtp.starttls()
		smtp.login(SMTP_USERNAME, SMTP_PASSWORD)
		smtp.sendmail(email_from, email_to, email_message.as_string())
		smtp.quit()
		return HttpResponse(status=200)

from django.core.files.images import ImageFile

@csrf_exempt
def test(request):
	if request.method=='POST':
		# print request.body
		print request.FILES
		file_key=None
		for file_key in sorted(request.FILES):
			pass

		print file_key
		wrapped_file = ImageFile(request.FILES[file_key])
		filename = wrapped_file.name
		print filename

		# # new photo table-row 
		photo = Photo()
		photo.filename = filename
		photo.image = request.FILES[file_key]
		photo.save()
		return HttpResponse()

				



