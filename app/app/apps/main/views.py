from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse


def main(request):
    return render(request, 'main/main.html')


def add_img(request):
    if request.method == 'POST':
        form = OurImgForm(request.POST, request.FILES)

        if form.is_valid():
            cd = form.cleaned_data
            new_photo = OurImg(img=cd['img'])
            new_photo.name = new_photo.img.name
            new_photo.save()
            return HttpResponseRedirect(reverse('main:main'))
    else:
        form = OurImgForm()
    return render(request, 'main/add_img.html', {'form': form})


def display_imgs(request):
    if request.method == 'GET':
        imgs = OurImg.objects.all()
        return render(request, 'main/display_imgs.html', {'imgs': imgs})


def delete_img(request, img_id):
    cur_img = None
    try:
        cur_img = OurImg.objects.get(id=img_id)
    except:
        raise Http404('ERROR item_delete')

    cur_img.delete()

    return HttpResponseRedirect(reverse('main:display_imgs'))
