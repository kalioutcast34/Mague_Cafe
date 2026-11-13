from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('menu/', views.menu, name='menu'),
	path('stay/', views.stay, name='stay'),
	path('heritage/', views.heritage, name='heritage'),
	path('trail-guide/', views.trail_guide, name='trail_guide'),
	path('gallery/', views.gallery, name='gallery'),
	path('guestbook/', views.guestbook, name='guestbook'),
	path('contact/', views.contact, name='contact'),
	path('book-table/', views.book_table, name='book_table'),
]