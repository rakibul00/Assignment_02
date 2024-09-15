from django.urls import path
#from book.views import home,store_book,show_book,edit_book,delet_book
from . import views
urlpatterns = [
    
    path('',views.home),
    path('store_new_book/',views.store_book, name='storebook'),
    path('show_book/',views.show_book, name='showbook'),
    path('edit_book/<int:id>',views.edit_book, name='edit_book'),
    path('delet_book/<int:id>',views.delet_book, name='delet_book'),
    path('complete/',views.complete,name='complete')
]











