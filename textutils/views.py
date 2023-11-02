from django.http import  HttpResponse
from django.shortcuts import render



def index(request):
    params ={'name':'Sam', 'place':'Mars'}
    return render(request,'index.html',params)

def analyze(request):
    # Get the text
    djtext= request.POST.get('text','default')

    #Check checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')

    #Check which checkbox is on
    if removepunc=='on' or fullcaps=="on" or newlineremover=="on" or extraspaceremover == "on" or charcounter == "on":
        if removepunc=='on':
            punctuations = '''!()-[]{};:'"\,<>.|=/?@#$%^&*_~'''
            analyzed =""
            for char in djtext:
                if char not in punctuations:
                    analyzed+=char
            params={'purpose':'Removed Punctuations','analyzed_text': analyzed}
            # return render(request,'analyze.html',params)
            djtext=analyzed


        if(fullcaps=="on"):
            analyzed=""
            for char in djtext:
                analyzed= analyzed + char.upper()

            params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}

            djtext = analyzed
        if(newlineremover=="on"):
            analyzed = ""
            for char in djtext:
                if char !="\n" and char!="\r":
                    analyzed = analyzed + char

            params = {'purpose': 'Remove Newline', 'analyzed_text': analyzed}
            djtext = analyzed
        if (extraspaceremover == "on"):
            analyzed = ""
            for index in range(len(djtext)-1):
                if not ( djtext[index]==" " and djtext[index+1 ] ==" " ):
                    analyzed = analyzed + djtext[index]
            params = {'purpose': 'Remove Newline', 'analyzed_text': analyzed}
            djtext = analyzed

        if (charcounter == "on"):
            analyzed = 0
            for index in range(len(djtext)):
                if not ( djtext[index]==" "):
                    analyzed = analyzed + 1
            params = {'purpose': 'Remove Newline', 'analyzed_text': analyzed}


    else:
        return HttpResponse("Please select any operation")

    return render(request, 'analyze.html', params)
