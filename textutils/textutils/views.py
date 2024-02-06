from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    django_text = request.GET.get('text', 'default')

    # Check checkbox values
    remove_punctuation = request.GET.get('removepunc', 'off')
    full_capitalization = request.GET.get('fullcaps', 'off')
    new_line_remover = request.GET.get('newlineremover', 'off')
    extra_space_remover = request.GET.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if remove_punctuation == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in django_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        django_text = analyzed
        # return render(request, 'analyze.html', params)

    if full_capitalization=="on":
        analyzed = ""
        for char in django_text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        django_text = analyzed
        # return render(request, 'analyze.html', params)

    if extra_space_remover=="on":
        analyzed = ""
        for index, char in enumerate(django_text):
            if not(django_text[index] == " " and django_text[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        django_text = analyzed
        # return render(request, 'analyze.html', params)

    if new_line_remover == "on":
        analyzed = ""
        for char in django_text:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        django_text = analyzed
        # return render(request, 'analyze.html', params)

    if remove_punctuation != "on" and new_line_remover != "on" and extra_space_remover !="on" and full_capitalization !="on":
        return HttpResponse("please select any operation and try again")

    return  render(request, 'analyze.html', params)

