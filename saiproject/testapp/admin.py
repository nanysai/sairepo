from django.contrib import admin
from testapp.models import School,College,Degree

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['sno','sname','sclass','sadr','scl']
admin.site.register(School,SchoolAdmin)

class CollegeAdmin(admin.ModelAdmin):
    list_display = ['sno','sname','sclass','sadr','college']
admin.site.register(College,CollegeAdmin)

class DegreeAdmin(admin.ModelAdmin):
    list_display = ['sno','sname','sclass','sadr','degree']
admin.site.register(Degree,DegreeAdmin)

