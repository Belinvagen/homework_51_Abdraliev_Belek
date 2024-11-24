from django.shortcuts import render, redirect
from .models import Cat

cat_instance = None

def welcome(request):
    if request.method == 'POST':
        cat_name = request.POST.get('cat_name')
        global cat_instance
        cat_instance = Cat(name=cat_name)
        return redirect('cat_status')
    return render(request, 'cat_app/welcome.html')

def cat_status(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if cat_instance:
            cat_instance.perform_action(action)
    return render(request, 'cat_app/cat_status.html', {'cat': cat_instance})
