from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'core/home.html')

def menu(request):
	return render(request, 'core/menu.html')

def stay(request):
	return render(request, 'core/stay.html')

def heritage(request):
	return render(request, 'core/heritage.html')

def trail_guide(request):
	return render(request, 'core/trail_guide.html')

def gallery(request):
	return render(request, 'core/gallery.html')

def guestbook(request):
	return render(request, 'core/guestbook.html')

def contact(request):
	return render(request, 'core/contact.html')

def book_table(request): 
	return render(request, 'core/book_table.html')