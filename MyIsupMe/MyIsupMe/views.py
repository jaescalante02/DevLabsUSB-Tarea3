from django.http import HttpResponse, HttpResponseRedirect
import datetime
import urllib
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render

#View que despliega la pagina de inicio del sistema
def home(request):
  now= datetime.datetime.now()
  return render (request,'index.html',{'now':now})

def errores(request):
  now= datetime.datetime.now()
  return render (request,'error.html',{'now':now})

def verificacionredirect(request):
    webpage=request.POST['webpage']
    return HttpResponseRedirect("http://54.209.102.149:19080/verificacion/" + webpage + "/")


def verificacion(request,webpage):
    #webpage=request.POST['webpage']
    if(not (':' in webpage)):
        webpage = 'http://' + webpage
    now= datetime.datetime.now()
    if (('.' in webpage) and (len(webpage)>3)):
       #Reviso que el cliente no exista ya
      try:
          httpresp = urllib.urlopen(webpage).getcode()
          if(httpresp!=200):
              return render (request, 'fail.html', {'now':now, 'pag':webpage})                 
      except IOError:
          return render (request, 'fail.html', {'now':now, 'pag':webpage})             
 
      return render (request, 'success.html', {'now':now, 'pag':webpage})
    else:
      return render (request, 'incomplete.html', {'now':now})


