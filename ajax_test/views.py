from django.shortcuts import render

from media import image_cv2
from .forms import DemoForm


def image(request):
    if request.method == 'POST':
        form = DemoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = request.POST['name']
            image_aj = request.FILES['image']
            s = "./media/" + str(image_aj)
            list_img = image_cv2.compares(s)
            print(name)
    else:
        form = DemoForm()
        list_img = []
    return render(request, 'ajax/image_upload.html', {
        'form': form, 'list': list_img
    })
