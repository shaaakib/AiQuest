from django.contrib import admin
from About_Us.models import Teacher
class TeacherAdmin(admin.ModelAdmin):
 list_display=('id', 'tid', 'tname', 'temail')
#Register your models here.
admin.site.register(Teacher, TeacherAdmin)
