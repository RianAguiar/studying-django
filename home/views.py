from django.shortcuts import render

def home(request):
    print("home")
    context = {'text':'texto home usando variavel'}
    return render(request,'home/home.html',context)