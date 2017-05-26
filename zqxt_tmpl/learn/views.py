from django.shortcuts import render

# Create your views here.

def home(request):
    list1 = ['1',2,3,4,5,68,7,8]
    return render(request,'test.html',{'list1':list1})
