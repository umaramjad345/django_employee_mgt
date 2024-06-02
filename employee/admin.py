from django.contrib import admin
from .models import Emp, Testimonial
# Register your models here.


class EmpAdmin(admin.ModelAdmin):
    list_display = ['emp_id','name','phone','is_working']
    list_editable = ['is_working']
    search_fields = ['emp_id','name','phone']
    list_filter = ['is_working']

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'picture']
    list_editable = ['rating']
    search_fields = ['name']
    list_filter = ['rating']

admin.site.register(Emp, EmpAdmin)
admin.site.register(Testimonial, TestimonialAdmin)  