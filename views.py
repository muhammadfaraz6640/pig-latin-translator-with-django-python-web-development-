from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
'''
def hello(request):
    text="welcome to my app"
    return HttpResponse(text)
def morning(request,age):
    text="good morning  ...!!my age is "+str(age) 
    return HttpResponse(text)
def gello(request):
   today = datetime.datetime.now().date()
   return render(request, "gello.html", {"today" : today})
   '''
def home(request):
   return render(request,'home.html')
def translate(request):
   orignal=request.GET["orignaltext"]
   result=""
   sub=orignal.split()
   for word in sub:
      if word[0] in ['a','i','e','o','u']:
         result+=word + 'yay'
         result+=" "
      else:
         result += word[1:]
         result += word[0]
         result += 'ay'
         result+=" "
   return render(request,'second_page.html',{'orignal':orignal,'result': result})
'''
for d in sub:
      for a in d:
         if a=='a' or a=='i' or a=='o' or a=='e' or a=='u':
            b=d.index(a)
         text=d[b:]+d[:b]+'yay'
      result+=text 
      text=""
'''