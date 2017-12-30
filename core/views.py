from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from core.forms import DocumentForm, DemoForm

from core.models import Document, Demo
from media import image_cv2


def home(request):
    documents = Document.objects.all()
    number = len(image_cv2.myList)
    return render(request, 'core/home.html', {'documents': documents, 'number': number})


def main_page(request):
    return render(request, 'index.html', )


def main_page_logedin(request):
    return render(request, 'core/main_page.html', )


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })


def image(request):
    demos = Demo.objects.all()
    if request.method == 'POST':
        form = DemoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # image_cv2.compares(form)
            return redirect('home')
    else:
        form = DemoForm()
    return render(request, 'core/image.html', {
        'form': form, 'demos': demos
    })
