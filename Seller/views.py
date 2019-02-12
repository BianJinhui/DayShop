import os
from django.shortcuts import render,HttpResponseRedirect
from Seller.models import Seller,Store
from DayShop.views import saveFile
from DayShop.settings import MEDIA_ROOT

def login(request):
    return render(request,"seller/login.html")

def register(request):
    error = ""
    if request.method == "POST" and request.POST:
        postData = request.POST
        username = postData.get("username")
        password = postData.get("password")
        nickname = postData.get("nickname")
        phone = postData.get("phone")
        email = postData.get("email")
        photo = request.FILES.get("photo")
        seller = Seller()
        seller.seller_name = username
        seller.seller_password = password
        seller.seller_nickname = nickname
        seller.seller_phone = phone
        seller.seller_email = email
        seller.seller_photo = photo.name

        file_path = os.path.join(MEDIA_ROOT,photo.name)
        savefile = saveFile(photo,file_path)
        if savefile == "success":
            seller.save()
        else:
            error = savefile
    return render(request, "seller/register.html",{"error":error})

def register_store(request):
    hope_reffer = "http://"+request.META.get("HTTP_HOST")+"/seller/register/"
    if request.META.get("HTTP_REFERER") == hope_reffer:
        if request.method == "POST" and request.POST:
            return HttpResponseRedirect("/seller/login/")
        return render(request, "seller/register_store.html")
    else:
        return HttpResponseRedirect("/seller/register/")
    # error = ""
    # if request.method == "POST" and request.POST:
    #     postData = request.POST
    #     username = postData.get("username")
    #     password = postData.get("password")
    #     nickname = postData.get("nickname")
    #     phone = postData.get("phone")
    #     email = postData.get("email")
    #     photo = request.FILES.get("photo")
    #     seller = Seller()
    #     seller.seller_name = username
    #     seller.seller_password = password
    #     seller.seller_nickname = nickname
    #     seller.seller_phone = phone
    #     seller.seller_email = email
    #     seller.seller_photo = photo.name
    #
    #     file_path = os.path.join(MEDIA_ROOT,photo.name)
    #     savefile = saveFile(photo,file_path)
    #     if savefile == "success":
    #         seller.save()
    #     else:
    #         error = savefile
    # return render(request, "seller/register_store.html",{"error":request})

def logout(request):
    pass

def index(request):
    pass

# Create your views here.
