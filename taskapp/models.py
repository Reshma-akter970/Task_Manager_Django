from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models


PRIORITY_CHOICES=(
    ('Low', 'Low'),
    ('Medium','Medium'),
    ('High', 'High'),
)
LEVEL_CHOICES=(
    ('Done','Done'),
    ('Undone','Undone'),
)
# Create your models here.
class TaskModel(models.Model):
    title=models.CharField(max_length=250)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField( null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date=models.DateField()
    taskimage=models.ImageField(upload_to='TaskImage' ,blank=True)
    priority=models.CharField(choices=PRIORITY_CHOICES,max_length=100)
    level=models.CharField(choices=LEVEL_CHOICES, max_length=100,)

