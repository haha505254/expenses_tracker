from django.contrib import admin

# Register your models here.
from expenses_log.models import Expense

class ExpenseAdmin(admin.ModelAdmin):   
    list_display=('name','price')
    list_filter=('name','price')
    search_fields=('name',)
    

admin.site.register(Expense,ExpenseAdmin)