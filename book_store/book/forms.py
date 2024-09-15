from django import forms
from book.models import BookStoreModel
from book.models import TaskModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        fields = ['id','book_name','author','category']
        #excludu = ['first_pub','last_pub']
        
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']