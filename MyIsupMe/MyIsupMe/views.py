from django.http import HttpResponse
import datetime
import urllib
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render

#View que despliega la pagina de inicio del sistema
def home(request):
  now= datetime.datetime.now()
  return render (request,'index.html',{'now':now})

def verificacion(request):
    webpage=request.POST['webpage']
    if(not (':' in webpage)):
        webpage = 'http://' + webpage
    now= datetime.datetime.now()
    if (webpage):
       #Reviso que el cliente no exista ya
      try:
          httpresp = urllib.urlopen(webpage).getcode()  
      except IOError:
          return render (request, 'fail.html', {'now':now})             
 
      return render (request, 'success.html', {'now':now})
    else:
      return render (request, 'incomplete.html', {'now':now})


