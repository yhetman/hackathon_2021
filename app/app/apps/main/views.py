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

        directory = r'media/result'
        directories_m, files_m = get_paths(directory=directory)
        zip_name = zip_sorted_directories(directory=directory)
        return render(request, 'main/display_sorted_images.html', {'directories': directories_m,
                                                                   'files': files_m,
                                                                   'zip_name': zip_name})


def delete_image(request, img_id):
    cur_img = None

    try:
        cur_img = Photo.objects.get(id=img_id)
    except:
        raise Http404('ERROR item_delete')

    cur_img.delete()

    return HttpResponseRedirect(reverse('main:display_images'))


def download(request):
    zipFileName = 'sorted_photos.zip'
    content_type = "application/octet-stream"
    response = HttpResponse(zipFileName, content_type=content_type)

    response["Content-Disposition"] = "attachment; filename=" + str(zipFileName)
    return response


def get_paths(directory):
    import os, sys

    directories_m = []
    files_m = []

    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            print(os.path.join(root, subdirectory))
            directories_m.append(os.path.join(root, subdirectory))
        for file in files:
            print(os.path.join(root, file))
            files_m.append(os.path.join(root, file))

    return directories_m, files_m


def zip_sorted_directories(directory):
    from zipfile import ZipFile
    import os
    from os.path import basename

    zipFileName = 'sorted_photos.zip'
    with ZipFile(zipFileName, 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                filePath = os.path.join(folderName, filename)
                zipObj.write(filePath, basename(filePath))

    return zipFileName
