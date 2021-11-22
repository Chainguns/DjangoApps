from django.shortcuts import render
from . import translate
# Create your views here.
def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['text_area']
        lang = request.POST['languages_']
        output = translate.translate(original_text, lang)
        return render(request, 'translator.html', {'output_text': output, 'original_text': original_text})
    else:
        return render(request, 'translator.html')