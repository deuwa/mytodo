from typing import Text
from django.db import models

# Create your models here.

class Todolist(models.Model):
    Text = models.CharField(max_length=45)
    complited = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Text  
        
        