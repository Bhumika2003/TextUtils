

from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    new_line_remover=request.POST.get('remover','off')
    spaceremover=request.POST.get('extraspaceremover','off')
    
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;?@[\]^_`{|}~,<>'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
               analyzed=analyzed+char
        params = {'purpose':'Remove Punctutions...','analyzed_text':analyzed}
        djtext = analyzed
    
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose':'Change to UpperCase...','analyzed_text':analyzed}
        djtext = analyzed
    
    if(new_line_remover=="on"):
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
              analyzed=analyzed+char
        params = {'purpose':'Removed newlines...','analyzed_text':analyzed}
        djtext = analyzed
    
    if(spaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
            
        params = {'purpose':'spaceremover...','analyzed_text':analyzed}
        djtext = analyzed
    
    if(removepunc!="on" and fullcaps!= "on" and new_line_remover!= "on" and spaceremover!= "on"):
        return HttpResponse("Error!,Please Select any operation and try again ")
    
    return render(request,'analyze.html',params)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


