from django.shortcuts import render
from School.models import Contact, Subject, Event, EventImage
from .forms import ClassSelectionForm
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def home(request):
    return render(request, "index.html")


def aboutus(request):
    return render(request, "about.html")


def course(request):
    return render(request, "courses.html")


def events(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, "events.html", context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        description = request.POST['description']
        # print('post worked')
        contact = Contact(name=name, email=email, phone=phone, desc=description)
        contact.save()
        messages.success(request, 'Form Submitted Successfully!')

    return render(request, "contact.html")


def classes(request, class_name):
    # selected_class = Class.objects.get(name=class_name)
    subjects = Subject.objects.filter(name=class_name)
    return render(request, 'classes.html', {'class_name': class_name, 'subjects': subjects})
    # subjects = Subject.objects.filter(classes__name=class_name)
    # return render(request, 'classes.html', {'class_name': class_name, 'subjects': subjects})