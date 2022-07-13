from django.contrib import admin
from .models import Lista, Task
# Register your models here.
admin.site.register([Lista, Task])