from django.shortcuts import render

from media import image_cv2
from .forms import DemoForm


def image(request):
    if request.method == 'POST':
        name = request.POST['name']
        image_aj = request.FILES['image']
        form = DemoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            print(name)
            s = "./media/" + str(image_aj)
            list_img = image_cv2.compares(s)
    else:
        form = DemoForm()
        list_img = []
    return render(request, 'ajax/image_upload.html', {
        'form': form, 'list': list_img
    })
