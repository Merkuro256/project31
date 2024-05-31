from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'elements/index.html')

@login_required
def elements(request):
    return render(request, 'elements/elements.html')

@login_required
def first_lesson(request):
    return render(request, 'elements/first_lesson.html')

@login_required
def second_lesson(request):
    return render(request, 'elements/second_lesson.html')

@login_required
def third_lesson(request):
    return render(request, 'elements/third_lesson.html')

def test_context(request):
    context = {
        'title': 'Teach',
        'header':'Добро пожаловать!',
        'username':'Божко Артем',
    }
    return render(request, 'elements/test-context.html', context)