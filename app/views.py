from django.shortcuts import render

# Create your views here.
def data(request):
    data = 'Hello'
    d = {'assumption':data}    
    return render(request,'index.html',context=d)

def login(request):
    d = {'name' : 'swayam' , 'age' : 22}
    return render(request, 'login.html', context=d)