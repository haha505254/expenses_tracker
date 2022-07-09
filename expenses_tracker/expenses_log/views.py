from django.http import HttpResponse
from django.shortcuts import render,redirect
from expenses_log.models import Expense

# Create your views here.
def index(request):
    return render(request,'expenses_log/index.html')

def listall(request):  
    expenses = Expense.objects.all().order_by('id')  
    #讀取資料表, 依 id 遞增排序(欄位前加入負號-id代表遞減排序)
    return render(request, "expenses_log/index.html", locals())

def insert(request):  #新增資料
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            price = request.POST.get('price')
            unit = Expense.objects.create(name=name, price=price) 
            unit.save()  #寫入資料庫
    except Exception as e:
        return HttpResponse("請填入正確數字")
    expenses = Expense.objects.all().order_by('-id')  #讀取資料表, 依 id 遞減排序
    return redirect('listall')