from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
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


def delete_image(request, img_id):
    cur_img = None

    try:
        cur_img = Photo.objects.get(id=img_id)
    except:
        raise Http404('ERROR item_delete')

    cur_img.delete()

    return HttpResponseRedirect(reverse('main:display_images'))
