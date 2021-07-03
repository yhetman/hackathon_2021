from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from app.settings import MEDIA_ROOT, MEDIA_URL
from django.urls import reverse


def main(request):
    return render(request, 'main/main.html')


def add_images(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')

        for image in images:
            new_photo = Photo(image=image)
            new_photo.name = new_photo.image.name
            new_photo.save()

        return HttpResponseRedirect(reverse('main:display_images'))

    return render(request, 'main/add_images.html')


def display_images(request):
    if request.method == 'GET':
        images = Photo.objects.all()
        return render(request, 'main/display_images.html', {'imgs': images})

    if request.method == 'POST':
        # тут вставляйте методы

        directories_m, files_m = get_paths()
        return render(request, 'main/display_sorted_images.html', {'directories': directories_m,
                                                                   'files': files_m})


def delete_image(request, img_id):
    cur_img = None

    try:
        cur_img = Photo.objects.get(id=img_id)
    except:
        raise Http404('ERROR item_delete')

    cur_img.delete()

    return HttpResponseRedirect(reverse('main:display_images'))


def get_paths():
    import os, sys
    directory = r'media/result'
    directories_m = []
    files_m = []
    i = 0
    j = 0
    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            print(os.path.join(root, subdirectory))
            directories_m.append(os.path.join(root, subdirectory))
        for file in files:
            print(os.path.join(root, file))
            files_m.append(os.path.join(root, file))

    print(directories_m)
    print(files_m)

    return directories_m, files_m