from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, Teams

# Create your views here.
#def demo(request):
    #return render(request,"index.html")
#def about(request):
    #return render(request,"about.html")
#def contact(request):
    #return HttpResponse("Hello Iam Contact")

# to pass a value
#def demo(request):
  #  name="india"
  #  return render(request,"index.html",{'obj':name})
#def addition(request):
   # x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
   # res=x+y
  #  return render(request,"result.html",{'result':res})
def demo(request):

   obj=Place.objects.all()
   teamobj=Teams.objects.all()
   return render(request,"index.html",{'result':obj, 'teamresult':teamobj})
