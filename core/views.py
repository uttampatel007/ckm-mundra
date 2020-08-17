from django.shortcuts import render
from . models import Contact

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
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		message = request.POST.get('comment')

		c = Contact(name=name,email=email,subject=subject,message=message)
		c.save()

		submit_message = " આભાર. અમે જલ્દી જ તમારો સંપર્ક કરીશું."
		context = {'submit_message':submit_message}
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