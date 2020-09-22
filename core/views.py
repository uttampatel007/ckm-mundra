from django.shortcuts import render
from . models import Contact
from ckm.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def home(request):
	return render(request,'core/index.html')

def admission(request):
	return render(request,'core/admission.html')

def gallery(request):
	return render(request, 'core/gallery.html')

def result(request):
	return render(request, 'core/results.html')

def contact(request):
	context = {}
	if request.method == "POST":
		name = request.POST.get('author')
		message = request.POST.get('comment')
		address = request.POST.get('address')
		phone = request.POST.get('phone')

		c = Contact(name=name,phone=phone,message=message,address=address)
		c.save()

		submit_message = " સંદેશ/અભિપ્રાય બદલ આભાર. અમે જલ્દી જ તમારો સંપર્ક કરીશું."
		context = {'submit_message':submit_message}
		# subject = "SCHOOL WEBSITE CONTACT"
		# recepient = 'uttam11.velani11@gmail.com'
		# message1 = 'Message From website \n NAME : %s \n ADDRESS : %s \n PHONE: %s \n MESSAGE: %s' %(name,address,phone,message)
		# send_mail(subject, message1, EMAIL_HOST_USER, [recepient], f	ail_silently = False)

		return render(request, 'core/contact.html',context)
	else:
		return render(request, 'core/contact.html')
# 

def history(request):
	return render(request, 'core/about.html')
# 

def school_family(request):
	return render(request, 'core/schoolFamily.html')

def memories(request):
	return render(request, 'core/memories.html')

def co_curricular(request):
	return render(request, 'core/activity.html')