from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
  list_display = ("name_task", "des_task", "start_date_task", "statut_task")

admin.site.register(Task, TaskAdmin)