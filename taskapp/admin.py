from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TaskModel
@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display=['title', 'description','due_date','priority','level', 'taskimage']