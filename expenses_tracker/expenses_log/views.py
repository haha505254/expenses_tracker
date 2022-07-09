from django.shortcuts import render
from expenses_log.models import Expense

# Create your views here.
def index(request):
    return render(request,'expenses_log/index.html')

def listall(request):  
    expenses = Expense.objects.all().order_by('id')  
    #讀取資料表, 依 id 遞增排序(欄位前加入負號-id代表遞減排序)
    return render(request, "expenses_log/index.html", locals())