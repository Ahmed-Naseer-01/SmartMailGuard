from django.shortcuts import render
from .forms import EmailForm
from .utils import detect_spam

def classify_email(request):
    result = None
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email_text = form.cleaned_data['email_text']
            result = detect_spam(email_text)
    else:
        form = EmailForm()
    return render(request, 'classifier/classify_email.html', {'form': form, 'result': result})