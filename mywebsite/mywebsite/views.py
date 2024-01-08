from django.shortcuts import render
from django.http import HttpResponse


def handler1(request):
    return render(request, 'index.html', {'name': 'handler2'})


def handler2(request):
    val = (request.POST.get('text1', 'default'))
    val1 = (request.POST.get('removepunc', 'off'))
    val2 = (request.POST.get('uppercase', 'off'))
    val3 = (request.POST.get('newlinerem', 'off'))
    val4 = (request.POST.get('extraSpacerem', 'off'))
    transformations=[]
    flag=1
    if val1=='on':
      transformations.append('Punctuations Removed')
      ans=''
      flag=0
      for i in val:
        if i not in '''.,?!;'"()[]{}-+=/\&@#$%^*_|~`''':
          ans+=i
      val=ans

    if val2=='on':
      transformations.append('Uppercase')
      ans=''
      flag=0
      ans=val.upper()
      val=ans

    if val3=='on':
      transformations.append('New Lines Removed')
      flag=0
      ans=''
      for i in val:
        if i not in ['\n','\r']:
          ans+=i
      val=ans
      
    if val4=='on':
      transformations.append('Extra Space Removed')
      flag=0
      ans=''
      n=len(val)
      for i,data in enumerate(val):
        if i<n and not (val[i]==' ' and val[i+1]==' '):
          ans+=data
      val=ans
    if flag==1:
      ans=val
      transformations.append('No Transformation Applied')
    return render(request,'result.html',{'data':ans,'transformations':transformations})


def aboutUs(request):
  return render(request,'aboutUs.html')

def contactUs(request):
  return render(request,'Contact.html')