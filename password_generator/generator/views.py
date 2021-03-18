import random
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'abcd'})

def about(request):
    return render(request,'generator/about.html')



def password(request):
       # return HttpResponse('our first django page')
      myPassword=''
      characters= list('abcdefghijklmnopqrstuvwxyz')
      length =int(request.GET.get('length'))
      if request.GET.get('uppercase'):
            characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
      if request.GET.get('numbers'):
            characters.extend(list("0123456789"))
      if request.GET.get('specials'):
           characters.extend(list("~!@#$%^&*()_+{}[]:<>?"))

      for length in range(length):
            myPassword += random.choice(characters)

      return render(request, 'generator/password.html', {"password":myPassword})

# def password(request):
#     return render(request,'generator/password.html')