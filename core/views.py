from django.shortcuts import render

def home(requests):
	return render(requests,'core/index.html')

def admission(requests):
	return render(requests,'core/admission.html')

def gallery(requests):
	return render(requests, 'core/gallery.html')

def result(requests):
	return render(requests, 'core/results.html')

def contact(requests):
	return render(requests, 'core/contact.html')
# 

def history(requests):
	return render(requests, 'core/about.html')
# 

def school_family(requests):
	return render(requests, 'core/schoolFamily.html')

def memories(requests):
	return render(requests, 'core/memories.html')

def co_curricular(requests):
	return render(request, 'core/activity.html')