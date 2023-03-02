from pathlib import PosixPath
from django.shortcuts import render
from django.http import HttpResponse
from numpy.core.fromnumeric import reshape
from numpy.lib.npyio import save
from .models import m_user, single_img, user_img
import csv
from io import TextIOWrapper, StringIO
import cv2
from PIL import Image
import os, sys
from . import cen
import numpy as np
from .forms import UpLoadProfileImgForm, SUpLoadProfileImgForm
import glob
from django.conf import settings
from sklearn.metrics.pairwise import cosine_similarity



# Create your views here.

def index(request):
    #Formから画像を受け取る
    if request.method != 'POST':
        img_path = []
        filename = []
        center = 0
        form = UpLoadProfileImgForm()
        context = {
            'form': form
        }
    else:
        form = UpLoadProfileImgForm(request.POST, request.FILES)
        if form.is_valid():
            img_1 = form.cleaned_data['img_1']
            img_2 = form.cleaned_data['img_2']
            img_3 = form.cleaned_data['img_3']
            userImg = user_img()
            userImg.img1 = img_1
            userImg.img2 = img_2
            userImg.img3 = img_3
            userImg.save()
        
        img_path = glob.glob('C:/Users/norimasa/recom/web/mysite/media/images/*')
        filename  = []
        txts = []
        for x in img_path:
            name = os.path.basename(x)
            n = "media/images/" + name
            filename.append(n)
            name = name.split('.', 1)[0]
            m = 'C:/Users/norimasa/recom/web/mysite/reco/txt/' + name + '.npy'
            txts.append(m)

        #重心を計算
        center = cen.get_center(txts)
        center = center.reshape(1, -1)
        #center = kcenter_255.get_center(img_path)
        #ディレクトリからファイルの読み込み
        user_path = glob.glob('C:/Users/norimasa/recom/web/mysite/static/men/*/')
        #テキストファイルの読み込み
        result = {}
        for a in user_path:
            dname = os.path.basename(os.path.dirname(a))
            #numpy配列として読み取り
            dcenter = np.load(a + 'center.npy')
            dcenter = dcenter.reshape(1, -1)
            hdis = cosine_similarity(center, dcenter)
            result[dname] = hdis
        
        test = sorted(result.items(), key=lambda x:x[1])[0:10]
        #resultから近いユーザー10人取得
        reco = []
        for key, v in sorted(result.items(), key=lambda x:x[1], reverse=True)[0:10]:
            udir = glob.glob('C:/Users/norimasa/recom/web/mysite/static/men/' + key + '/*.jpg')
            u = []
            for b in udir:
                dname = os.path.basename(b)
                u.append('men/'+ key + '/' + dname)
            u.insert(0, key)
            reco.append(u)
            

        context = {
        'form': form,
        'filename': filename,
        'res': reco,
        'test': test
        }
        return render(request, 'reco/result.html', context)
    return render(request, 'reco/recommend.html', context)


def single(request):
    if request.method != 'POST':
        form = SUpLoadProfileImgForm()
        context = {
            'form': form
        }
    else:
        form = SUpLoadProfileImgForm(request.POST, request.FILES)
        if form.is_valid():
            img_1 = form.cleaned_data['img_1']
            userImg = single_img()
            userImg.img = img_1
            userImg.save()
        
        img_path = glob.glob('C:/Users/norimasa/recom/web/mysite/media/SImg/*')
        filename  = []
        for x in img_path:
            name = os.path.basename(x)
            n = "../media/Simg/" + name
            filename.append(n)
        
        target = 'C:/Users/norimasa/recom/web/mysite/reco/txt/' + os.path.basename(img_path[0]).split('.', 1)[0] + '.npy'
        #重心を計算
        center = cen.get_single(target)
        
        #ディレクトリからファイルの読み込み
        user_path = glob.glob('C:/Users/norimasa/recom/web/mysite/reco/txt/*')
        result = {}
        for a in user_path:
            dname = os.path.basename(a).split('.', 1)[0]
            dname = dname + '.jpg'
            dcenter = cen.get_single(a)
            #距離の計算と格納
            hdis = cosine_similarity(center, dcenter)
            #hdis = np.linalg.norm(center - dcenter)
            result[dname] = hdis
        
        test = sorted(result.items(), key=lambda x:x[1], reverse=True)[0:10]
        #resultから近いユーザー10人取得
        reco = []
        for key, v in sorted(result.items(), key=lambda x:x[1], reverse=True)[1:11]:
        #for key, v in sorted(result.items(), key=lambda x:x[1])[0:10]:
           reco.append([key, 'single/' + key])
        
        context = {
        'form': form,
        'filename': filename,
        'res': reco,
        'test': test
        }
        
        return render(request, 'reco/result_sin.html', context)
    return render(request, 'reco/recommend_sin.html', context)

def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for line in csv_file:
            m, created = m_user.objects.get_or_create(name=line[0])
            m.name = line[0]
            m.dir_path = line[1]
            m.save()

        return render(request, 'reco/upload.html')

    else:
        return render(request, 'reco/upload.html')