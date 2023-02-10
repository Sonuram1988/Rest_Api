from django.contrib import admin
from .models import Company,Employee
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','about','type')
    search_fields=('name',)
    list_filter=('name','type',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','address','email','phone','about','type')
    search_fields=('name',)
    list_filter=('name','type',)


admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)




