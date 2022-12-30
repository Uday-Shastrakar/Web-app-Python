from django.shortcuts import render, HttpResponse

#Create your views here.
def index(request):
    context= {
        'variable': "this is variable"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is homepage")
   

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is servicess")

def contact(request):
    return render(request,'contact.html')
    # return HttpResponse("this is contact")