from __future__ import print_function
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
import cv2
from django.conf import settings
from PIL import Image
import numpy as np
from .face_mozaic import face_mozaic


def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DocumentForm()
        max_id = Document.objects.latest('id').id
        obj = Document.objects.get(id = max_id)

        input = settings.BASE_DIR + obj.photo.url
        output = settings.BASE_DIR + "/media/output/output.jpg"
        face_mozaic(input, output)
    #import pdb; pdb.set_trace() 
    return render(request, 'app1/index.html', {
        'form': form,
        'obj':Document.objects.get(id = max_id),
    })
    import pdb; pdb.set_trace()  
