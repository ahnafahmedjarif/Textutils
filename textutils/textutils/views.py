from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # params = {'name':'jarif', 'place':'mars'}
    return render(request, "index.html")

def analyze(request):
    # Get the text from the textarea and store it to django_text variable
    django_text = request.GET.get('text', 'default')
    remove_punctuation = request.GET.get('remove_punctuation', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    new_line_remover = request.GET.get('new_line_remover', 'off')

    # Analyze the text
    if remove_punctuation == "on":
        punctuations = '''!()-[];:'"\,/<>?@#$%^&*_~'''
        analyzed = ""
        for char in django_text:
            if char not in punctuations:
                analyzed += char
        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    elif uppercase == "on":
        analyzed = ""
        for char in django_text:
            analyzed += char.upper()
        params = {'purpose':'Uppercase', 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    elif new_line_remover == "on":
        analyzed = ""
        for char in django_text:
            if char != "\n":
                analyzed += char
        params = {'purpose': 'New line Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

