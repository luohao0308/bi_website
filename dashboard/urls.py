# -*- coding: utf-8 -*-
# @Author: ander
# @Date:   2021-07-19 12:26:04
# @Last Modified by:   ander
# @Last Modified time: 2021-08-10 19:02:34
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("api/order/filter", views.order_filter_api),
    path("api/order/data_vis", views.order_data_vis_api),
    path("api/order/send_email", views.order_send_email_api),
    path("api/spider/zhihu", views.spider_zhihu_api),
]
