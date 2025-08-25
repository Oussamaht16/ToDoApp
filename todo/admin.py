from .models import Task
from django.contrib import admin

# Register your models here.

#hadi bch fl admin db ibanolk g3 les column li 3ndk f db o kyn wkhdokhrin kima search baro mazal wkhdokhrin
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task' , 'is_completed' , 'updated_at')
    search_fields = ('task',)


admin.site.register(Task , TaskAdmin)