from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
    CATEGORY = (
        ('Physicas','physics'),
         ('Bangla','Bangla'),
          ('English','English'), 
        ('Math','Math'),
       ('Polictis','Polictis'),
       ('Science','Science'),       
    )
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=30, choices=CATEGORY)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
    
    
    
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)

   