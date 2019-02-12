#coding:utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class GoodsType(models.Model):
    type_tag = models.CharField(max_length = 32,verbose_name = "类型名称")
    type_parent_id = models.IntegerField(verbose_name = "父类型")
    type_description = models.TextField(verbose_name = "类型描述")

class Store(models.Model):
    """
    店铺表
    卖家只能注册一个店铺
    注册店铺先要注册成为卖家
    """
    store_name = models.CharField(max_length = 32,verbose_name = "店铺名称")
    store_address = models.TextField(verbose_name = "店铺地址")
    store_logo = models.ImageField(upload_to = "images",verbose_name = "店铺logo")
    seller_id = models.IntegerField(verbose_name = "卖家")


class Seller(models.Model):
    """
    卖家表
    """
    seller_name = models.CharField(max_length = 32,verbose_name = "卖家用户名")
    seller_password = models.CharField(max_length = 32,verbose_name = "卖家密码")
    seller_nickname = models.CharField(max_length = 32,verbose_name = "卖家昵称")
    seller_phone = models.CharField(max_length = 32,verbose_name = "卖家电话")
    seller_photo = models.ImageField(upload_to = "images", verbose_name="卖家头像")
    seller_email = models.EmailField(verbose_name = "卖家邮箱")

class Goods(models.Model):
    """
    商品表
    """
    goods_name = models.CharField(max_length = 32,verbose_name = "商品名称")
    goods_id = models.CharField(max_length = 32, verbose_name = "商品编号")
    goods_price = models.FloatField(verbose_name = "商品价格")
    goods_nprice = models.FloatField(verbose_name = "商品现价")
    goods_num = models.IntegerField(verbose_name = "商品数量")
    goods_description = RichTextUploadingField(verbose_name = "商品简介")
    goods_content = RichTextUploadingField(verbose_name = "商品详情")
    goods_time = models.DateField(verbose_name = "上架时间")
    goods_picture = models.ImageField(upload_to = "images", verbose_name = "商品图片")

    seller = models.ForeignKey(GoodsType,on_delete = models.CASCADE,verbose_name = "对应类型")
    store = models.ForeignKey(Store,on_delete = models.CASCADE,verbose_name = "对应店铺")

class Picture(models.Model):
    picture_tag = models.CharField(max_length = 32,verbose_name = "图片名称")
    picture_src = models.CharField(max_length = 32,verbose_name = "图片地址")
    picture_dec = models.TextField(verbose_name = "图片描述")

    goods = models.ForeignKey(Goods,on_delete = models.CASCADE,verbose_name = "对应商品")

# Create your models here.
