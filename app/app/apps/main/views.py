from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse
from .exif_sorter import get_images_paths, get_meta, add_clusters_by_date, add_clusters_by_gps
from .clarity import clusters_by_clarity
from .sort_images import sort_images

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

        import os, sys
        directory = r'media/result'

        directories_m = []
        files_m = []

        for root, subdirectories, files in os.walk(directory):
            for subdirectory in subdirectories:
                print(os.path.join(root, subdirectory))
                directories_m.append(os.path.join(root, subdirectory))
            for file in files:
                print(os.path.join(root, file))
                files_m.append(os.path.join(root, file))
                
        print(directories_m)
        print(files_m)

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



